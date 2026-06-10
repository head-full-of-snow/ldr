"""
Local Deep Research (LDR) 统一调用客户端

支持两种调用模式:
  - "api":    通过 REST API 调用远程 LDR Web 服务（需要服务运行在 5000 端口）
  - "python": 通过 import local_deep_research 直接调用（需要服务器 conda 环境）

支持两种研究力度:
  - "quick": 快速摘要（quick_summary），同步返回
  - "full":  完整报告（generate_report），耗时较长

使用示例:
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

    # 快速研究
    result = client.research("量子计算的最新进展", research_level="quick")

    # 完整报告并保存到文件
    result = client.research(
        "人工智能在医疗领域的应用综述",
        output_path="./report.md",
        research_level="full",
    )
"""

from __future__ import annotations

import logging
import os
import pickle
import re
import tempfile
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import requests

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 枚举与数据类
# ---------------------------------------------------------------------------

class Mode(str, Enum):
    API = "api"
    PYTHON = "python"


class ResearchLevel(str, Enum):
    QUICK = "quick"
    FULL = "full"


@dataclass
class ResearchResult:
    """统一的研究返回结构"""
    research_id: str
    summary: str
    content: str  # 完整内容（quick 时为 formatted_findings，full 时为 markdown 报告）
    sources: list[dict] = field(default_factory=list)
    findings: list[dict] = field(default_factory=list)
    iterations: int = 1
    raw: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# 主客户端类
# ---------------------------------------------------------------------------

class LDRClient:
    """
    Local Deep Research 统一调用客户端。

    Parameters
    ----------
    mode : str
        调用模式，"api" 或 "python"。
    base_url : str
        LDR Web 服务地址（mode="api" 时必填）。
    username : str
        登录用户名（mode="api" 时必填）。
    password : str
        登录密码（mode="api" 时必填）。
    provider : str
        LLM 提供商，如 "openai_endpoint"。
    api_key : str
        LLM API Key。
    model_name : str
        模型名称，如 "MiniMax-M2.7"。
    llm_url : str
        OpenAI 兼容端点 URL（provider 为 openai_endpoint 时使用）。
    search_tool : str
        搜索引擎，默认 "auto"。
    temperature : float
        LLM 采样温度。
    max_search_results : int
        最大搜索结果数。
    timeout : int
        HTTP 请求超时（秒），默认 300。
    """

    def __init__(
        self,
        mode: str = "api",
        base_url: str = "http://10.10.20.21:5000",
        username: str = "zxh",
        password: str = "@zxh19859769907",
        provider: str = "openai_endpoint",
        api_key: str = "sk-cp-GcVnQghbFoX36MYgx-mlE7-HA08JzvvnD6fh0f8iKTUKLDa5wq10ybwR3mKBoGT1ULTuBEaoMc1g1u9CH7zMexXk-vWzyKy30nWpoQGg-WmboBwRjMZ6m3U",
        model_name: str = "qwen3.6-35b-a3b",
        llm_url: str = "http://10.10.20.21:9090/v1",
        search_tool: str = "auto",
        temperature: float = 0.7,
        max_search_results: int = 10,
        timeout: int = 900,
    ):
        self.mode = Mode(mode)
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.provider = provider
        self.api_key = api_key
        self.model_name = model_name
        self.llm_url = llm_url
        self.search_tool = search_tool
        self.temperature = temperature
        self.max_search_results = max_search_results
        self.timeout = timeout

        # API 模式的 session（延迟初始化）
        self._session: requests.Session | None = None
        self._logged_in = False

        # Cookie 持久化路径（避免频繁登录触发限流）
        self._cookie_file = os.path.join(
            tempfile.gettempdir(),
            f".ldr_cookie_{username}.pkl"
        )

    # ======================================================================
    # 公开接口：主体函数
    # ======================================================================

    def research(
        self,
        query: str,
        output_path: str | None = None,
        research_level: str = "quick",
        iterations: int | None = None,
        searches_per_section: int = 2,
        research_id: str | None = None,
        **kwargs: Any,
    ) -> ResearchResult:
        """
        执行深度研究并返回结果。

        Parameters
        ----------
        query : str
            研究问题。
        output_path : str | None
            结果保存路径。为 None 时不保存文件。
            两种模式均保存为排版后的 Markdown（.md）文件。
        research_level : str
            研究力度，"quick"（快速摘要）或 "full"（完整报告）。
        iterations : int | None
            搜索迭代轮数。None 时使用默认值（quick=1, full=3）。
        searches_per_section : int
            每个章节的搜索次数（仅 full 模式）。
        research_id : str | None
            自定义研究 ID，默认自动生成。
        **kwargs
            传递给底层调用的额外参数。

        Returns
        -------
        ResearchResult
            统一的研究结果对象。
        """
        level = ResearchLevel(research_level)
        if research_id is None:
            research_id = str(uuid.uuid4())

        logger.info("开始研究 [%s] 模式=%s 力度=%s", research_id,
                    self.mode.value, level.value)

        if self.mode == Mode.API:
            result = self._research_via_api(
                query, level, iterations, searches_per_section, research_id, **kwargs)
        else:
            result = self._research_via_python(
                query, level, iterations, searches_per_section, research_id, **kwargs)

        result.research_id = research_id

        # 保存到文件
        if output_path:
            self._save_result(result, output_path, level)

        logger.info("研究完成 [%s]", research_id)
        return result

    # ======================================================================
    # API 模式实现
    # ======================================================================

    def _ensure_session(self) -> requests.Session:
        """确保已登录并返回可用的 requests.Session

        优先尝试加载持久化的 cookie，避免每次脚本调用都触发登录（限流 5次/15分钟）。
        Cookie 失效后自动重新登录。
        """
        if self._session is not None and self._logged_in:
            # 验证 session 是否仍然有效
            try:
                resp = self._session.get(f"{self.base_url}/api/v1/health")
                if resp.status_code == 200:
                    return self._session
            except Exception:
                pass
            # session 失效，清除并重连
            self._session = None
            self._logged_in = False

        self._session = requests.Session()
        self._session.verify = False  # 如有自签名证书可按需调整

        # 尝试从文件加载 cookie（pickle 序列化）
        if os.path.exists(self._cookie_file):
            try:
                with open(self._cookie_file, "rb") as f:
                    saved_cookies = pickle.load(f)
                self._session.cookies.update(saved_cookies)
                logger.info("已加载持久化 cookie")

                # 验证持久化 cookie 是否仍然有效（避免每次触发登录）
                resp = self._session.get(f"{self.base_url}/api/v1/health")
                if resp.status_code == 200:
                    self._logged_in = True
                    logger.info("Cookie 有效，跳过登录流程")
                    return self._session
                else:
                    logger.info("Cookie 已失效，需要重新登录")
            except Exception as e:
                logger.debug(f"加载/验证 cookie 失败: {e}")

        # Step 1: 访问登录页获取 cookie 和 CSRF token
        login_page = self._session.get(f"{self.base_url}/auth/login")
        login_page.raise_for_status()

        csrf_match = re.search(
            r'name="csrf_token"\s+value="([^"]+)"', login_page.text)
        if not csrf_match:
            raise RuntimeError("无法从登录页面提取 CSRF token")
        csrf_token = csrf_match.group(1)

        # Step 2: 提交登录
        resp = self._session.post(
            f"{self.base_url}/auth/login",
            data={
                "username": self.username,
                "password": self.password,
                "csrf_token": csrf_token,
            },
            allow_redirects=False,
        )
        # 302 重定向表示登录成功
        if resp.status_code not in (302, 303, 200):
            raise RuntimeError(
                f"登录失败，HTTP {resp.status_code}: {resp.text[:200]}")

        self._logged_in = True

        # 持久化 cookie 到文件，避免下次重新登录
        try:
            with open(self._cookie_file, "wb") as f:
                pickle.dump(self._session.cookies, f)
            logger.info(f"Cookie 已持久化到: {self._cookie_file}")
        except Exception:
            pass

        logger.info("API 模式登录成功")
        return self._session

    def _research_via_api(
        self,
        query: str,
        level: ResearchLevel,
        iterations: int | None,
        searches_per_section: int,
        research_id: str,
        model_name: str = "qwen3.6-35b-a3b",
        **kwargs: Any,
    ) -> ResearchResult:
        """通过 REST API v1 调用。

        API 模式下的完整流程:
          1. 登录并维护 Session Cookie
          2. 调用 /api/v1/generate_report（full 模式）或 /api/v1/quick_summary（quick 模式）
          3. 解析 JSON 响应
          4. 将 Markdown 内容保存到文件（如指定 output_path）

        生成排版完备 PDF 的方式:
          方案 A — 调用下载 API（推荐）:
            拿到 research_id 后，POST /api/v1/research/<id>/export/pdf
            返回二进制 PDF 文件，自带 WeasyPrint 渲染的 CSS 样式
          方案 B — 本地用 Markdown 生成:
            用 result.content（Markdown 文本）通过任何 MD→PDF 工具转换
        """
        session = self._ensure_session()
        headers = {"Content-Type": "application/json"}

        if level == ResearchLevel.QUICK:
            endpoint = f"{self.base_url}/api/v1/quick_summary"
            payload: dict[str, Any] = {
                "query": query,
                "iterations": iterations or 1,
                "temperature": self.temperature,
            }
        else:
            endpoint = f"{self.base_url}/api/v1/generate_report"
            payload = {
                "query": query,
                "searches_per_section": searches_per_section,
                "temperature": self.temperature,
                "model_name": model_name,
            }

        payload.update(kwargs)

        logger.info("调用 API: %s，query=%s", endpoint, query[:80])
        resp = session.post(endpoint, headers=headers,
                            json=payload, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()

        logger.info("API 响应 keys: %s", list(data.keys()))
        if "content" in data:
            logger.info("响应 content 长度: %d 字符", len(data["content"]))
        if "metadata" in data:
            logger.info("响应 metadata: %s", data["metadata"])

        return self._parse_api_response(data, level)

    def _parse_api_response(self, data: dict, level: ResearchLevel) -> ResearchResult:
        """解析 API 返回的 JSON 为统一的 ResearchResult。

        full 模式（generate_report）返回格式:
          {
            "content": "# Table of Contents\n...\n# Section 1\n...",  # 完整 Markdown 报告
            "metadata": {"generated_at": "...", "query": "...", ...},
            "file_path": "/path/to/report.md"  # 仅当 output_file 参数提供时存在
          }

        quick 模式（quick_summary）返回格式:
          {
            "summary": "...",
            "formatted_findings": "...",  # 格式化后的发现列表
            "findings": [...],
            "sources": [...],
            "iterations": 1
          }
        """
        content = data.get("formatted_findings", "") or data.get("content", "")
        return ResearchResult(
            research_id=data.get("research_id", ""),
            summary=data.get("summary", ""),
            content=content,
            sources=data.get("sources", []),
            findings=data.get("findings", []),
            iterations=data.get("iterations", 0),
            raw=data,
        )

    # ======================================================================
    # Python 直接调用模式实现
    # ======================================================================

    def _build_settings_override(self, **extra: Any) -> dict:
        """构造 settings_override 字典"""
        settings: dict[str, Any] = {
            "llm.model": self.model_name,
            "llm.provider": self.provider,
        }
        if self.llm_url:
            settings["llm.openai_endpoint.url"] = self.llm_url
        if self.search_tool:
            settings["search.tool"] = self.search_tool
        if self.max_search_results:
            settings["search.max_results"] = self.max_search_results
        settings.update(extra)
        return settings

    def _research_via_python(
        self,
        query: str,
        level: ResearchLevel,
        iterations: int | None,
        searches_per_section: int,
        research_id: str,
        **kwargs: Any,
    ) -> ResearchResult:
        """通过 import local_deep_research 直接调用。

        Python 模式流程:
          1. from local_deep_research.api import generate_report / quick_summary
          2. 调用 generate_report(query, settings_override=..., searches_per_section=...)
          3. 返回 dict: {"content": "完整 Markdown", "metadata": {...}}

        生成排版完备 PDF 的方式:
          方案 A — 本地调用 PDFService:
            from local_deep_research.web.services.pdf_service import get_pdf_service
            pdf_service = get_pdf_service()
            pdf_bytes = pdf_service.markdown_to_pdf(result.content, title="标题")
          方案 B — 调用 LDR 导出 API:
            session.post(f"{self.base_url}/api/v1/research/{research_id}/export/pdf")
        """
        try:
            from local_deep_research.api import generate_report, quick_summary
        except ImportError as e:
            raise ImportError(
                "无法导入 local_deep_research，请确认已安装并处于正确的 conda 环境中。"
            ) from e

        settings_override = self._build_settings_override(
            **{
                "search.iterations": iterations or (1 if level == ResearchLevel.QUICK else 3),
                "search.questions_per_iteration": searches_per_section,
            }
        )

        common_kwargs: dict[str, Any] = {
            "provider": self.provider,
            "api_key": self.api_key,
            "settings_override": settings_override,
            "research_id": research_id,
        }
        common_kwargs.update(kwargs)

        if level == ResearchLevel.QUICK:
            common_kwargs["temperature"] = self.temperature
            data = quick_summary(query, **common_kwargs)
        else:
            common_kwargs["temperature"] = self.temperature
            data = generate_report(query, **common_kwargs)

        logger.info("Python 模式响应 keys: %s", list(data.keys()))
        if "content" in data:
            logger.info("content 长度: %d 字符", len(data["content"]))
        if "metadata" in data:
            logger.info("metadata: %s", data["metadata"])

        return self._parse_python_response(data, level)

    def _parse_python_response(self, data: dict, level: ResearchLevel) -> ResearchResult:
        """解析 Python 直接调用的返回值。

        full 模式（generate_report）返回:
          {"content": "完整 Markdown", "metadata": {...}}
        quick 模式（quick_summary）返回:
          {"summary": "...", "formatted_findings": "...", "findings": [...]}
        """
        content = data.get("formatted_findings", "") or data.get("content", "")
        return ResearchResult(
            research_id=data.get("research_id", ""),
            summary=data.get("summary", ""),
            content=content,
            sources=data.get("sources", []),
            findings=data.get("findings", []),
            iterations=data.get("iterations", 0),
            raw=data,
        )

    # ======================================================================
    # 结果保存
    # ======================================================================

    @staticmethod
    def _save_result(result: ResearchResult, output_path: str, level: ResearchLevel) -> None:
        """将结果保存到文件。

        保存规则:
          - full 模式: 保存为 Markdown（.md），包含目录、章节、Sources
          - quick 模式: 保存为 Markdown（.md），包含摘要和格式化发现
          - 两种模式均使用 .md 格式，确保排版可读
        """
        if "/" in output_path:
            output_dir = os.path.dirname(output_path)
        else:
            output_dir = "ldr_result"
            output_path = os.path.join(output_dir, output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # 两种模式都保存为排版后的 Markdown 文件
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result.content)

        logger.info("排版后的 Markdown 报告已保存到: %s (%d 字符)",
                    output_path, len(result.content))
        logger.info("研究 ID: %s, 来源数: %d, 迭代轮数: %d",
                    result.research_id, len(result.sources), result.iterations)

    # ======================================================================
    # 辅助方法
    # ======================================================================

    def health_check(self) -> dict:
        """检查 API 健康状态（仅 API 模式可用，无需登录）"""
        if self.mode != Mode.API:
            raise ValueError("health_check 仅支持 API 模式")
        resp = requests.get(f"{self.base_url}/api/v1/health", timeout=10)
        resp.raise_for_status()
        return resp.json()

    def __repr__(self) -> str:
        return (
            f"LDRClient(mode={self.mode.value!r}, "
            f"base_url={self.base_url!r}, "
            f"model={self.model_name!r})"
        )


if __name__ == "__main__":
    # 简单测试
    ldr = LDRClient()
    session = ldr._ensure_session()
    headers = {"Content-Type": "application/json"}
    base_url = ldr.base_url
    query = "AI编程"
    health_result = requests.get("http://10.10.20.21:5000/api/v1/health")
    print("健康检查结果", health_result)
    # result = ldr.research(query, research_level="full",
    #                       output_path="arxiv_search_method_aicode.md", search_tool="arxiv")
    # result = ldr.research(query, research_level="full",
    #                       output_path="auto_search_method_aicode.md", search_tool="auto")
    result = ldr.research(query, research_level="quick",
                          output_path="searxng_search_method_aicode.md", search_tool="searxng")
    # parallel_scientific,auto,arxiv
    print("研究结果", result)
