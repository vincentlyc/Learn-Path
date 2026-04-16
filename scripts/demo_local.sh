#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory

from llm_dataplatform.databricks import build_pipeline, query_pipeline

with TemporaryDirectory() as d:
    base = Path(d)
    (base / "adr_001.md").write_text(
        "Use governed feature store policies for model traceability in regulated workflows.",
        encoding="utf-8",
    )
    pipeline = build_pipeline(data_path=str(base))
    pipeline.index_adr_directory(namespace="demo")
    print(query_pipeline(pipeline, "model traceability policies for deployment", namespace="demo"))
PY
