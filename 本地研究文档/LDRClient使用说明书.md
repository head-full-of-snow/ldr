# LDRClient 使用说明书

> Local Deep Research (LDR) 统一调用客户端，封装 REST API 与 Python 直接调用两种模式，提供简洁的研究接口。

---

## 目录

1. [概述](#1-概述)
2. [安装与依赖](#2-安装与依赖)
3. [快速开始](#3-快速开始)
4. [构造参数详解](#4-构造参数详解)
5. [主体函数 research() 详解](#5-主体函数-research-详解)
6. [返回值 ResearchResult 详解](#6-返回值-researchresult-详解)
7. [两种模式详解](#7-两种模式详解)
8. [使用示例](#8-使用示例)
9. [辅助方法](#9-辅助方法)
10. [注意事项与常见问题](#10-注意事项与常见问题)
11. [环境变量参考](#11-环境变量参考)
12. [API 端点参考](#12-api-端点参考)

---

## 1. 概述

`LDRClient` 是对 Local Deep Research 项目的封装客户端类，屏蔽了底层调用差异，提供统一的 `research()` 接口。

### 核心能力

| 维度 | 选项 | 说明 |
|------|------|------|
| **调用模式** | `"api"` | 通过 HTTP 调用远程 LDR Web 服务（5000 端口） |
| | `"python"` | 直接 import `local_deep_research` 包调用（需 conda 环境） |
| **研究力度** | `"quick"` | 快速摘要，约 30 秒返回，保存为 `.md` |
| | `"full"` | 完整报告，生成排版完备的 Markdown 格式（含目录、章节），耗时数分钟 |

### 两种模式对比

| 对比维度 | API 模式 | Python 模式 |
|----------|----------|-------------|
| 需要 Web 服务 | 是（5000 端口） | 否 |
| 认证方式 | 用户名密码自动登录 | 不需要 |
| 运行位置 | 任意能访问服务器的机器 | 必须在安装了 LDR 的服务器上 |
| 执行方式 | 同步 HTTP 请求 | 同步函数调用 |
| 适用场景 | 远程调用、脚本自动化 | 服务器端批处理、深度定制 |

---

## 2. 安装与依赖

### Python 依赖

```bash
pip install requests
```

### 文件放置

将 `ldr_client.py` 放置在项目目录中，然后导入：

```python
from ldr_client import LDRClient, ResearchResult
```

### Python 模式额外要求

如果使用 `mode="python"`，需要：

1. SSH 到服务器 `10.10.20.21`
2. 激活 conda 环境：`conda activate ldr`
3. 在服务器端运行脚本

---

## 3. 快速开始

### 3.1 API 模式 — 快速研究

```python
from ldr_client import LDRClient

client = LDRClient(
    mode="api",
    base_url="http://10.10.20.21:5000",
    username="zxh",
    password="@zxh19859769907",
    provider="openai_endpoint",
    api_key="sk-cp-xxx...",
    model_name="MiniMax-M2.7",
    llm_url="https://api.minimaxi.com/v1",
)

result = client.research("量子计算的最新进展")
print(result.summary)
```

### 3.2 Python 模式 — 快速研究

```python
from ldr_client import LDRClient

client = LDRClient(
    mode="python",
    provider="openai_endpoint",
    api_key="sk-cp-xxx...",
    model_name="MiniMax-M2.7",
    llm_url="https://api.minimaxi.com/v1",
)

result = client.research("深度学习的最新进展")
print(result.summary)
```

### 3.3 完整报告并保存

```python
result = client.research(
    "人工智能在医疗领域的应用综述",
    output_path="./output/report.md",
    research_level="full",
)

print(f"报告已保存，共 {len(result.sources)} 个来源")
```

---

## 4. 构造参数详解

### `LDRClient(...)` 参数列表

```python
client = LDRClient(
    mode="api",                # 调用模式："api" 或 "python"
    base_url="http://10.10.20.21:5000",  # LDR 服务地址（api 模式必填）
    username="zxh",            # 登录用户名（api 模式必填）
    password="@zxh19859769907",# 登录密码（api 模式必填）
    provider="openai_endpoint",# LLM 提供商
    api_key="sk-cp-xxx...",    # LLM API Key
    model_name="MiniMax-M2.7", # 模型名称
    llm_url="https://api.minimaxi.com/v1",  # OpenAI 兼容端点 URL
    search_tool="auto",        # 搜索引擎
    temperature=0.7,           # LLM 采样温度
    max_search_results=10,     # 最大搜索结果数
    timeout=300,               # HTTP 请求超时（秒）
)
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `mode` | `str` | `"api"` | 调用模式。`"api"` 通过 HTTP 调用远程服务，`"python"` 直接导入包调用 |
| `base_url` | `str` | `"http://10.10.20.21:5000"` | LDR Web 服务地址，`mode="api"` 时必填 |
| `username` | `str` | `""` | 登录用户名，`mode="api"` 时必填 |
| `password` | `str` | `""` | 登录密码，`mode="api"` 时必填 |
| `provider` | `str` | `"openai_endpoint"` | LLM 提供商，可选 `openai_endpoint`、`openai`、`anthropic`、`ollama` 等 |
| `api_key` | `str` | `""` | LLM 服务的 API Key |
| `model_name` | `str` | `"MiniMax-M2.7"` | 使用的模型名称 |
| `llm_url` | `str` | `"https://api.minimaxi.com/v1"` | OpenAI 兼容端点的 URL |
| `search_tool` | `str` | `"auto"` | 搜索引擎，可选 `auto`、`searxng`、`wikipedia` 等 |
| `temperature` | `float` | `0.7` | LLM 采样温度，越高越随机 |
| `max_search_results` | `int` | `10` | 单次搜索返回的最大结果数 |
| `timeout` | `int` | `300` | HTTP 请求超时时间（秒），`full` 模式建议设大一些 |

---

## 5. 主体函数 research() 详解

### 函数签名

```python
def research(
    query: str,                          # 研究问题（必填）
    output_path: str | None = None,      # 结果保存路径
    research_level: str = "quick",       # 研究力度："quick" 或 "full"
    iterations: int | None = None,       # 搜索迭代轮数
    searches_per_section: int = 2,       # 每个章节的搜索次数（仅 full）
    research_id: str | None = None,      # 自定义研究 ID
    **kwargs,                            # 传递给底层的额外参数
) -> ResearchResult
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `query` | `str` | — | **必填**。要研究的问题或主题 |
| `output_path` | `str \| None` | `None` | 结果保存路径。`None` 时不保存文件。两种模式均保存为排版后的 Markdown（`.md`）格式 |
| `research_level` | `str` | `"quick"` | 研究力度。`"quick"` 为快速摘要，`"full"` 为完整报告 |
| `iterations` | `int \| None` | `None` | 搜索迭代轮数。`None` 时 quick 默认 1，full 默认 3。值越大研究越深入 |
| `searches_per_section` | `int` | `2` | 每个章节的搜索次数，仅 `research_level="full"` 时生效 |
| `research_id` | `str \| None` | `None` | 自定义研究 ID。`None` 时自动生成 UUID |
| `**kwargs` | — | — | 传递给底层 API 或 Python 函数的额外参数 |

### research_level 对比

| 项目 | `"quick"` | `"full"` |
|------|-----------|----------|
| 底层调用 | `quick_summary` | `generate_report` |
| 返回内容 | 摘要 + 发现列表 + 来源 | 完整 Markdown 报告 |
| 耗时 | 约 30 秒 | 数分钟 |
| iterations 默认值 | 1 | 3 |
| 保存格式 | Markdown（.md） | Markdown（.md） |
| 适用场景 | 快速了解某个主题 | 生成完整的研究报告文档 |

---

## 6. 返回值 ResearchResult 详解

`research()` 返回一个 `ResearchResult` 数据对象，结构如下：

```python
@dataclass
class ResearchResult:
    research_id: str          # 研究唯一 ID
    summary: str              # 研究摘要文本
    content: str              # 完整内容（quick 时为 formatted_findings，full 时为 Markdown 报告）
    sources: list[dict]       # 来源列表，每项包含标题、URL 等信息
    findings: list[dict]      # 分阶段发现列表
    iterations: int           # 实际迭代次数
    raw: dict                 # 原始返回数据（完整 JSON）
```

### 访问示例

```python
result = client.research("量子计算的最新进展")

# 摘要
print(result.summary)

# 完整格式化内容
print(result.content)

# 来源数量
print(f"共引用 {len(result.sources)} 个来源")

# 遍历来源
for src in result.sources:
    print(f"  - {src.get('title', '未知')}")

# 遍历发现
for finding in result.findings:
    print(f"  - {finding.get('text', '')}")

# 原始数据
print(result.raw)
```

---

## 7. 两种模式详解

### 7.1 API 模式 (`mode="api"`)

**工作流程：**

```
LDRClient.research()
  │
  ├─ 1. _ensure_session()
  │     ├─ GET /auth/login → 获取登录页 + CSRF token
  │     └─ POST /auth/login → 提交登录，获取 Session Cookie
  │
  ├─ 2. POST /api/v1/quick_summary   （research_level="quick"）
  │    或 POST /api/v1/generate_report（research_level="full"）
  │
  ├─ 3. 解析 JSON 返回 → ResearchResult
  │
  └─ 4. 可选：保存到 output_path
```

**特点：**
- 自动处理登录、CSRF token、Session Cookie
- Session 登录状态在多次调用间复用，不会重复登录
- 需要远程 LDR Web 服务正在运行（默认 5000 端口）
- 可从任何能访问服务器的机器上调用

### 7.2 Python 模式 (`mode="python"`)

**工作流程：**

```
LDRClient.research()
  │
  ├─ 1. from local_deep_research.api import quick_summary / generate_report
  │
  ├─ 2. 构造 settings_override（含 model、provider、url 等）
  │
  ├─ 3. 调用 quick_summary()   （research_level="quick"）
  │    或 generate_report()    （research_level="full"）
  │
  ├─ 4. 解析返回 dict → ResearchResult
  │
  └─ 5. 可选：保存到 output_path
```

**特点：**
- 不依赖 Web 服务，不经过 HTTP
- 直接调用 Python 函数，效率更高
- 必须在安装了 `local_deep_research` 的服务器上运行
- 需要 conda 环境 `ldr`

---

## 8. 生成排版完备的 PDF 和 Markdown 研究报告

### 8.A 获取排版后的 Markdown

`research()` 返回的 `result.content` 即为 **完整排版的 Markdown 内容**，包括：

```
# Table of Contents
1. **引言**
   1.1 背景介绍
2. **核心技术**
   ...
## Sources
- [来源1](https://...)
- [来源2](https://...)
```

### 8.B 获取排版完备的 PDF

LDR 提供了两种 PDF 生成路径：

#### 方式 A — 调用导出 API（推荐，样式最精美）

```python
# Step 1: 先完成研究
result = client.research("量子计算的最新进展", research_level="full")
research_id = result.research_id

# Step 2: 调用导出 API 获取 PDF
import requests
resp = requests.post(
    f"{client.base_url}/api/v1/research/{research_id}/export/pdf",
    cookies=client._session.cookies,  # 复用登录 session
    timeout=300,
)
resp.raise_for_status()

# 保存 PDF
with open("report.pdf", "wb") as f:
    f.write(resp.content)
print(f"PDF 已生成，大小: {len(resp.content)} 字节")
```

导出 API 的底层管线：

```
Markdown 报告
    ↓
Python-Markdown 解析（tables, fenced_code, toc, footnotes 等扩展）
    ↓
HTML 文档（含 <!DOCTYPE>, <head>, <meta charset>）
    ↓
WeasyPrint + 内置 CSS（A4 页面、多字体回退、代码高亮）
    ↓
二进制 PDF 文件
```

#### 方式 B — Python 模式本地调用 PDFService

```python
from local_deep_research.web.services.pdf_service import get_pdf_service

pdf_service = get_pdf_service()
pdf_bytes = pdf_service.markdown_to_pdf(
    markdown_content=result.content,
    title="量子计算的最新进展",
    metadata={"author": "Your Name"},
)

with open("report.pdf", "wb") as f:
    f.write(pdf_bytes)
```

#### 方式 C — 命令行调用导出 API

```bash
# 先运行研究获取 research_id
RESEARCH_ID=$(python run_research.py --query "量子计算" --level full --output report.md | grep RESEARCH_ID | cut -d' ' -f2)

# 再导出 PDF
curl -X POST "http://10.10.20.21:5000/api/v1/research/${RESEARCH_ID}/export/pdf" \
     -H "Cookie: session=YOUR_SESSION_COOKIE" \
     -o report.pdf
```

### 8.C 其他导出格式

| 格式 | API 路径 | 说明 |
|------|----------|------|
| LaTeX | `export/latex` | 生成 `.tex` 文件，适合学术论文 |
| Quarto | `export/quarto` | 生成 `.zip`（含 `.qmd` + `.bib`），可用 Quarto 渲染为 PDF/HTML |
| ODT | `export/odt` | LibreOffice 格式，通过 Pandoc 转换 |
| RIS | `export/ris` | Zotero 文献格式 |

### 8.1 最简调用

### 8.1 最简调用

```python
from ldr_client import LDRClient

client = LDRClient(
    mode="api",
    base_url="http://10.10.20.21:5000",
    username="zxh",
    password="@zxh19859769907",
    provider="openai_endpoint",
    api_key="sk-cp-xxx...",
    model_name="MiniMax-M2.7",
    llm_url="https://api.minimaxi.com/v1",
)

result = client.research("什么是量子计算")
print(result.summary)
```

### 8.2 快速研究并保存 JSON

```python
result = client.research(
    "大语言模型的对齐技术",
    output_path="./results/alignment.json",
    research_level="quick",
    iterations=2,
)
print(f"摘要: {result.summary}")
print(f"来源: {len(result.sources)} 个")
```

保存的 JSON 文件内容格式：

```json
{
  "research_id": "70a0876e-...",
  "summary": "大语言模型的对齐技术是指...",
  "content": "## 详细发现\n...",
  "sources": [
    {"title": "...", "url": "..."}
  ],
  "findings": [...],
  "iterations": 2
}
```

### 8.3 完整报告保存为 Markdown

```python
result = client.research(
    "人工智能在医疗领域的应用综述",
    output_path="./reports/ai_medical.md",
    research_level="full",
    iterations=3,
    searches_per_section=3,
    timeout=600,
)
print(f"报告已生成，共 {result.iterations} 轮迭代")
```

### 8.4 批量研究

```python
topics = [
    "Transformer 架构的最新改进",
    "多模态大模型的发展现状",
    "AI Agent 技术综述",
]

for topic in topics:
    result = client.research(
        topic,
        output_path=f"./results/{topic[:20]}.json",
        research_level="quick",
    )
    print(f"[{result.research_id}] {topic} → {len(result.sources)} 个来源")
```

### 8.5 使用自定义研究 ID

```python
result = client.research(
    "深度强化学习应用",
    research_id="my-custom-id-001",
)
print(result.research_id)  # "my-custom-id-001"
```

### 8.6 Python 模式（在服务器上运行）

```python
# 需要在服务器上：ssh zengxinghang@10.10.20.21 → conda activate ldr
from ldr_client import LDRClient

client = LDRClient(
    mode="python",
    provider="openai_endpoint",
    api_key="sk-cp-xxx...",
    model_name="MiniMax-M2.7",
    llm_url="https://api.minimaxi.com/v1",
)

result = client.research(
    "量子计算的最新进展",
    output_path="/tmp/quantum_report.md",
    research_level="full",
)
```

### 8.7 切换搜索引擎

```python
# 使用 Wikipedia 搜索（无需额外服务）
client = LDRClient(
    mode="python",
    search_tool="wikipedia",
    # ... 其他参数
)
```

### 8.8 通过环境变量配置（Python 模式）

设置环境变量后，构造时可省略部分参数：

```bash
export LDR_LLM_PROVIDER=openai_endpoint
export LDR_LLM_MODEL=MiniMax-M2.7
export LDR_LLM_OPENAI_ENDPOINT_API_KEY=sk-cp-xxx...
export LDR_LLM_OPENAI_ENDPOINT_URL=https://api.minimaxi.com/v1
```

```python
# 环境变量已设置时，可简化构造
client = LDRClient(mode="python")
result = client.research("量子计算")
```

### 8.9 通过 REST API 导出已完成的研究报告

```python
import requests

# 复用已建立的 session
session = requests.Session()

# 登录
login_page = session.get("http://10.10.20.21:5000/auth/login")
# ... 提取 CSRF token 并提交登录（同 _ensure_session 逻辑）

# 获取已完成的研究记录
resp = session.get("http://10.10.20.21:5000/api/history")
researches = resp.json()["items"]

# 导出为 PDF
for r in researches:
    rid = r["id"]
    resp = session.post(f"http://10.10.20.21:5000/api/v1/research/{rid}/export/pdf")
    if resp.status_code == 200:
        with open(f"report_{rid}.pdf", "wb") as f:
            f.write(resp.content)
    resp = session.post(f"http://10.10.20.21:5000/api/v1/research/{rid}/export/latex")
    if resp.status_code == 200:
        with open(f"report_{rid}.tex", "wb") as f:
            f.write(resp.content)
```

---

## 9. 辅助方法

### health_check()

检查远程 LDR 服务是否在线（仅 API 模式）。

```python
client = LDRClient(mode="api", base_url="http://10.10.20.21:5000")
status = client.health_check()
# 返回: {"status": "ok", "message": "API is running", "timestamp": "..."}
```

### __repr__()

打印客户端摘要信息。

```python
print(client)
# LDRClient(mode='api', base_url='http://10.10.20.21:5000', model='MiniMax-M2.7')
```

---

## 10. 注意事项与常见问题

### 必须配置模型

`model_name` 不能为空，否则底层会抛出 `ValueError: LLM model not configured`。

```python
# 正确
client = LDRClient(model_name="MiniMax-M2.7", ...)

# 错误 — 会报错
client = LDRClient(model_name="", ...)
```

### 搜索引擎依赖

默认搜索引擎为 `searxng`，需要运行 SearXNG 实例。如果搜索服务不可用，研究仍能运行但搜索结果为空。

可切换为 Wikipedia 搜索（无需额外服务）：

```python
client = LDRClient(search_tool="wikipedia", ...)
```

### full 模式耗时较长

完整报告生成涉及多轮搜索和综合，通常需要数分钟。建议：

- 调大 `timeout`：`timeout=600`
- 在异步任务或 tmux 会话中运行

### API 模式登录失败

- 确认 `base_url` 可访问：先在浏览器打开 `http://10.10.20.21:5000`
- 确认 `username` 和 `password` 正确
- 确认 LDR Web 服务正在运行

### Python 模式导入失败

- 确认已激活 conda 环境：`conda activate ldr`
- 确认在项目目录下运行，或 `local_deep_research` 已正确安装

### 输出路径

- `output_path` 为 `None` 时不保存文件，仅返回 `ResearchResult` 对象
- 目录不存在时会自动创建
- 两种模式均保存为排版后的 Markdown（`.md`）格式

---

## 11. 环境变量参考

Python 模式下，以下环境变量可替代构造参数。命名规则：`LDR_` 前缀 + 设置键的 `.` 替换为 `_` + 全大写。

| 环境变量 | 说明 | 示例值 |
|----------|------|--------|
| `LDR_LLM_PROVIDER` | LLM 提供商 | `openai_endpoint` |
| `LDR_LLM_MODEL` | 模型名称（必填） | `MiniMax-M2.7` |
| `LDR_LLM_TEMPERATURE` | 采样温度 | `0.7` |
| `LDR_LLM_MAX_TOKENS` | 最大输出 tokens | `30000` |
| `LDR_LLM_OPENAI_ENDPOINT_URL` | OpenAI 兼容端点 | `https://api.minimaxi.com/v1` |
| `LDR_LLM_OPENAI_ENDPOINT_API_KEY` | 端点 API Key | `sk-cp-xxx...` |
| `LDR_SEARCH_TOOL` | 搜索引擎 | `searxng` / `auto` |
| `LDR_SEARCH_ITERATIONS` | 搜索迭代数 | `1` |
| `LDR_SEARCH_MAX_RESULTS` | 最大搜索结果 | `10` |

---

## 12. API 端点参考

### 研究生成

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/v1/quick_summary` | POST | 快速摘要，同步返回 |
| `/api/v1/generate_report` | POST | 完整报告，耗时较长 |
| `/api/v1/health` | GET | 健康检查，无需登录 |

### 导出（需要认证 Session）

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/v1/research/<id>/export/pdf` | POST | 导出为 PDF（WeasyPrint 渲染） |
| `/api/v1/research/<id>/export/latex` | POST | 导出为 LaTeX |
| `/api/v1/research/<id>/export/quarto` | POST | 导出为 Quarto（ZIP） |
| `/api/v1/research/<id>/export/odt` | POST | 导出为 ODT（LibreOffice） |
| `/api/v1/research/<id>/export/ris` | POST | 导出为 RIS（Zotero） |

### 管理

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/history` | GET | 获取研究历史记录 |
| `/api/research/<id>` | GET | 获取研究详情 |
| `/api/report/<id>` | GET | 获取研究报告内容（Markdown） |
| `/auth/login` | GET/POST | 登录认证 |

### Markdown 报告结构

`generate_report` 返回的 `content` 字段包含完整的排版后 Markdown，结构如下：

```markdown
# Table of Contents
1. **引言**
   1.1 背景介绍
2. **核心技术**
   2.1 原理
   2.2 现状
...

# Research Summary
This report was researched using an advanced search system...

# 1. 引言

## 1.1 背景介绍

[LLM 生成的详细内容...]

## Sources

- [来源标题](URL)
- [来源标题](URL)
```

---

> 文件位置：`ldr_client.py` | 服务版本：v1.6.9 | 服务器：10.10.20.21:5000
