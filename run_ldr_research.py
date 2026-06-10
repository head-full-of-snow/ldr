"""
Script to call Local Deep Research (LDR) API programmatically.
Uses LDR's internal SearchSystem -> AdvancedSearchSystem.
"""

import json
import os
import sys
import uuid
from pathlib import Path

# Force UTF-8 encoding for console output (Windows fix)
import io
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from loguru import logger

from local_deep_research.config.llm_config import get_llm
from local_deep_research.config.search_config import get_search
from local_deep_research.search_system import AdvancedSearchSystem
from local_deep_research.config.paths import get_research_outputs_directory


def run_research(query: str, mode: str = "quick"):
    """Run a deep research using LDR's internal API."""

    # --- Configuration ---
    model_provider = os.getenv("LDR_MODEL_PROVIDER", "ollama")
    model = os.getenv("LDR_MODEL", "qwen3.6-35b-a3")
    custom_endpoint = os.getenv("LDR_OPENAI_ENDPOINT", "http://localhost:11434/v1")
    search_engine = os.getenv("LDR_SEARCH_ENGINE", "arxiv")
    username = os.getenv("LDR_USERNAME", "default")
    iterations = int(os.getenv("LDR_ITERATIONS", "3"))
    questions_per_iteration = int(os.getenv("LDR_QUESTIONS", "3"))
    strategy = os.getenv("LDR_STRATEGY", "source-based")

    research_id = str(uuid.uuid4())[:8]
    output_dir = get_research_outputs_directory() / f"research_{research_id}"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[LDR] Research ID: {research_id}")
    print(f"[LDR] Query: {query}")
    print(f"[LDR] Mode: {mode}")
    print(f"[LDR] Provider: {model_provider}, Model: {model}")
    if model_provider == "openai_endpoint":
        print(f"[LDR] Endpoint: {custom_endpoint}")
    print(f"[LDR] Search Engine: {search_engine}")
    print(f"[LDR] Strategy: {strategy}")
    print(f"[LDR] Iterations: {iterations}")
    print()

    # --- Build complete settings_snapshot ---
    search_engines_config = {
        "ddg": {},
        "arxiv": {},
        "wikipedia": {},
        "pubmed": {},
        "searxng": {},
        "auto": {},
    }

    settings_snapshot = {
        "llm.provider": model_provider,
        "llm.model": model,
        "llm.temperature": 0.7,
        "llm.ollama.url": custom_endpoint,
        "llm.openai_endpoint.url": custom_endpoint,
        "llm.openai_endpoint.api_key": "not-needed",
        "llm.openai.api_key": "",
        "llm.anthropic.api_key": "",
        "llm.max_tokens": 100000,
        "llm.supports_max_tokens": True,
        "llm.streaming": False,
        "llm.max_retries": 3,
        "llm.request_timeout": 120,
        "search.engine.web": search_engines_config,
        "search.engine.auto": {},
        "search.tool": search_engine,
        "search.max_results": 10,
        "search.region": "wt-wt",
        "search.time_period": "all",
        "search.safe_search": True,
        "search.snippets_only": True,
        "search.search_language": "English",
    }

    # --- Progress callback ---
    def progress_callback(message, progress_percent, metadata):
        phase = metadata.get("phase", "")
        iter_num = metadata.get("iteration", "")
        prefix = f"[{phase.upper()}]" if phase else "[INFO]"
        if iter_num:
            prefix += f" (iter {iter_num})"
        # Replace any non-ASCII for console display
        clean_msg = message.encode("ascii", "replace").decode("ascii")
        print(f"{prefix} [{progress_percent}%] {clean_msg}")

    # --- Initialize LLM ---
    print("[LDR] Initializing LLM...")
    use_llm = get_llm(
        model_name=model,
        provider=model_provider,
        openai_endpoint_url=custom_endpoint,
        research_id=research_id,
        settings_snapshot=settings_snapshot,
    )
    print(f"[LDR] LLM initialized: {type(use_llm).__name__}")

    # --- Initialize Search Engine ---
    print("[LDR] Initializing search engine...")
    use_search = None
    for engine in [search_engine, "arxiv", "pubmed", "wikipedia"]:
        try:
            use_search = get_search(
                search_tool=engine,
                llm_instance=use_llm,
                username=username,
                settings_snapshot=settings_snapshot,
            )
            if use_search is not None:
                print(f"[LDR] Search engine '{engine}' initialized: {type(use_search).__name__}")
                break
            else:
                print(f"[LDR] Engine '{engine}' returned None, trying next...")
        except Exception as e:
            print(f"[LDR] Engine '{engine}' failed: {e}, trying next...")

    if use_search is None:
        print("[LDR] FATAL: No search engine available.")
        return None

    # --- Create Search System ---
    print("[LDR] Creating AdvancedSearchSystem...")
    system = AdvancedSearchSystem(
        llm=use_llm,
        search=use_search,
        strategy_name=strategy,
        max_iterations=iterations,
        questions_per_iteration=questions_per_iteration,
        username=username,
        research_id=research_id,
        programmatic_mode=True,
        search_original_query=True,
        settings_snapshot=settings_snapshot,
    )
    system.set_progress_callback(progress_callback)
    print("[LDR] System ready.\n")

    # --- Run Research ---
    print("[LDR] ===== Starting research =====\n")
    results = system.analyze_topic(query)
    print(f"\n[LDR] ===== Research complete =====")
    print(f"[LDR] Output dir: {output_dir}")

    # Save results as JSON
    results_path = output_dir / "raw_results.json"
    if isinstance(results, dict):
        for k, v in results.items():
            try:
                json.dumps(v)
            except TypeError:
                results[k] = str(v)[:500]
        with open(results_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"[LDR] Results saved to: {results_path}")
    else:
        with open(results_path, "w", encoding="utf-8") as f:
            f.write(str(results)[:50000])
        print(f"[LDR] Results saved to: {results_path}")

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_ldr_research.py \"<query>\"")
        sys.exit(1)

    query = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "quick"

    try:
        results = run_research(query, mode)
        print("\n[SUCCESS] Research completed successfully.")
    except Exception as e:
        print(f"\n[ERROR] Research failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
