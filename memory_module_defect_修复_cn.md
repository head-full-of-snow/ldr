# 历史记录/记忆模块 MemoryError 问题分析与修复方案

## 问题背景

用户在使用历史记录/记忆相关功能时遇到 `MemoryError`，错误发生在 SQLAlchemy 的 `cursor.execute()` 阶段：

```
MemoryError at sqlalchemy/engine/base.py in _exec_single_context
```

**根本原因**: 多个数据库查询一次性将所有 ORM 对象加载到内存中，导致内存溢出。

## 根因分析

### 问题1：`history_routes.py:54-65` — 查询加载了整个 `ResearchHistory` ORM 对象

```python
db_session.query(
    ResearchHistory,  # 加载所有列，包括 report_content (Text 大字段)
    func.count(Document.id).label("document_count"),
)
```

虽然限制了 200 条（上限 500），但 **`ResearchHistory` 是完整 ORM 对象**，包含 `report_content`（Text 字段）。每条详细研究报告可能很大（几 MB），200 条 × 几 MB 就可能超出内存限制。

### 问题2：`library_service.py:561-569` — 下拉框查询无 limit，加载全部历史

```python
session.query(ResearchHistory.id, ResearchHistory.title, ResearchHistory.query)
    .order_by(ResearchHistory.created_at.desc())
    .all()  # 无 limit！
```

下拉框选择器无分页地加载了**所有**历史记录。

### 问题3：`storage/database.py:131-134` — `list_reports()` 无分页

```python
results = self.session.query(ResearchHistory).filter(
    ResearchHistory.report_content.isnot(None)
).all()  # 加载所有有报告的研究记录，包含大字段
```

虽然返回时只取了部分字段，但查询加载了完整的 `ResearchHistory` 对象（含大字段）。

### 问题4：`library_service.py:360-391` 和 `library_rag_service.py:1747-1750` — 集合查询无 limit

- `library_service.py:360-391`：按集合加载文档，`.all()` 无 limit
- `library_rag_service.py:1747-1750`：加载集合所有 chunk，`.all()` 无 limit

## 修复方案

### 修复1：`src/local_deep_research/web/routes/history_routes.py`

**问题**: `query(ResearchHistory, ...)` 加载了 `report_content` 等大字段，但实际返回只用了 `id, title, query, mode, status, created_at, completed_at, duration_seconds, research_meta, chat_session_id`。

**方法**: 改为只查询需要的列，排除大字段：

```python
results = (
    db_session.query(
        ResearchHistory.id,
        ResearchHistory.title,
        ResearchHistory.query,
        ResearchHistory.mode,
        ResearchHistory.status,
        ResearchHistory.created_at,
        ResearchHistory.completed_at,
        ResearchHistory.duration_seconds,
        ResearchHistory.research_meta,
        ResearchHistory.chat_session_id,
        func.count(Document.id).label("document_count"),
    )
    .outerjoin(Document, Document.research_id == ResearchHistory.id)
    .group_by(ResearchHistory.id)
    .order_by(ResearchHistory.created_at.desc())
    .limit(limit)
    .offset(offset)
    .all()
)
```

然后将结果处理从 ORM 属性访问改为元组解包。

### 修复2：`src/local_deep_research/research_library/services/library_service.py`

**问题**: `get_research_list_for_dropdown()` 无 limit。

**方法**: 添加 `.limit(100)`（下拉框不需要全部数据）。

### 修复3：`src/local_deep_research/storage/database.py`

**问题**: `list_reports()` 加载完整 `ResearchHistory` 对象。

**方法**: 改为只查询需要的列（与修复1思路一致）。

### 修复4：`src/local_deep_research/research_library/services/library_service.py:360-391`

**方法**: 添加合理 limit（如 500）。

### 修复5：`src/local_deep_research/research_library/services/library_rag_service.py`

**方法**: 为 chunk 查询添加 limit 或使用 `.yield_per()` 流式处理。

## 验证方式

1. 确认所有涉及 `ResearchHistory` 的查询不再加载 `report_content` 等大字段（除非确实需要）
2. 所有 `query().all()` 都有合理的 limit 或分页
3. 运行现有测试确保行为不变
4. 手动测试历史记录页面加载（前端正常渲染）

## 需要修改的文件

| 文件 | 修改内容 |
|------|----------|
| `src/local_deep_research/web/routes/history_routes.py` | 查询指定列，排除大字段 |
| `src/local_deep_research/research_library/services/library_service.py` | 添加 limit |
| `src/local_deep_research/storage/database.py` | 查询指定列 |
| `src/local_deep_research/research_library/services/library_rag_service.py` | 添加 limit 或 yield_per |
