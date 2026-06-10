"""
Local Deep Research 执行脚本

供 local_deep_research 技能调用，封装 LDRClient.research() 的调用逻辑。
通过命令行参数接收研究配置，执行研究并输出结构化结果。

输出说明:
  - quick 模式: 输出摘要 + 格式化发现列表
  - full 模式:  输出完整 Markdown 报告（含目录、章节、Sources）
  - 结果文件统一保存为 .md 格式的排版后 Markdown 文件

用法:
    python run_research.py --query "研究问题" [--level quick|full] [--output PATH] [--iterations N]

获取排版完备 PDF 的方法:
  方式 A — 调用 LDR 导出 API:
    research_id=$(... run_research.py --query "xxx" --level full ...)
    curl -X POST http://localhost:5000/api/v1/research/$research_id/export/pdf \
         -H "Cookie: session=..." -o report.pdf
  方式 B — 使用 Python 本地转换:
    from ldr_client import LDRClient
    result = ldr.research("xxx", output_path="./report.md", research_level="full")
    # 然后用任何 MD→PDF 工具转换
"""

from ldr_client import LDRClient
import argparse
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Local Deep Research 执行脚本")
    parser.add_argument("--query", required=True, help="研究问题")
    parser.add_argument("--level", default="quick",
                        choices=["quick", "full"], help="研究力度 (默认: quick)")
    parser.add_argument(
        "--output", default="./ldr_result/output.md", help="结果保存路径 (默认: ./ldr_result/output.md)")
    parser.add_argument("--iterations", type=int, default=None, help="搜索迭代轮数")
    parser.add_argument("--search-tool", default=None,
                        help="搜索引擎 (arxiv, pubmed, openalex, parallel_scientific 等)")
    args = parser.parse_args()

    # 默认输出路径为当前目录的 output.md
    output_path = args.output
    logger.info("研究参数: query=%r level=%s output=%s iterations=%s search_tool=%s",
                args.query, args.level, output_path, args.iterations, args.search_tool)

    ldr = LDRClient(search_tool=args.search_tool or "auto")

    result = ldr.research(
        query=args.query,
        research_level=args.level,
        output_path=output_path,
        iterations=args.iterations,
    )

    # 结构化输出，供 SKILL 解析
    print("RESEARCH_ID:", result.research_id)
    print("SUMMARY:", result.summary)
    print("SOURCES_COUNT:", len(result.sources))
    print("ITERATIONS:", result.iterations)
    print("OUTPUT_FILE:", output_path)

    print("CONTENT_START")
    print(result.content)
    print("CONTENT_END")

    print("SOURCES_START")
    for src in result.sources:
        title = src.get("title", "")
        url = src.get("url", "")
        print(f"{title} ||| {url}")
    print("SOURCES_END")


if __name__ == "__main__":
    main()
