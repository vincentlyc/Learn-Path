# LLM Dataplatform Project Pack

An enterprise-ready, modular repository for building **Architecture Decision Record (ADR) Retrieval-Augmented Generation (RAG)** workflows on Databricks.

This project is intentionally packaged to support:
- **Platform and AI Engineering leadership** in semiconductor organizations (design ops, knowledge reuse, auditability).
- **Risk, compliance, and architecture governance** in financial institutions (traceability, explainability, controlled rollout).
- Hiring visibility for teams seeking candidates who can bridge **LLM systems, data platforms, and production engineering**.

## Why this structure works in enterprise settings

- **Modular package-first design**: logic lives in `src/`, not notebooks.
- **Notebook compatibility**: notebooks are thin orchestration shells, ideal for Databricks users.
- **Config-driven pipeline**: same code path can run in notebook demos and scheduled jobs.
- **Separation of concerns**: ingestion, retrieval, and generation are independently testable.

## Repository Layout

```text
.
├── docs/
│   └── architecture/
│       ├── architecture-overview.md
│       └── architecture-diagram-placeholder.drawio
├── notebooks/
│   ├── 01_setup_and_config.py
│   ├── 02_index_adr_documents.py
│   └── 03_query_and_generate.py
├── src/llm_dataplatform/
│   ├── adapters/
│   │   ├── llm_adapter.py
│   │   └── vector_store.py
│   ├── core/
│   │   ├── config.py
│   │   ├── models.py
│   │   └── text_processing.py
│   ├── pipelines/
│   │   └── adr_rag_pipeline.py
│   └── databricks.py
├── tests/
│   └── test_pipeline.py
├── pyproject.toml
└── README.md
```

## Concise Demo Path (Databricks)

1. Open `notebooks/01_setup_and_config.py` and set your ADR source path.
2. Run `notebooks/02_index_adr_documents.py` to chunk and index ADRs.
3. Run `notebooks/03_query_and_generate.py` with a leadership-facing query such as:
   - "What ADR decisions impact PCI and model risk controls?"
   - "Which architecture choices improve yield analytics and reduce fab-cycle latency?"

> Notebook files are in Databricks source format (`# Databricks notebook source`) so they can be imported directly.

## Quick Start (local or Databricks Repos)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## Positioning for Semiconductor and Financial Leadership

When presenting this project:
- Highlight the **decision traceability loop** from ADR ingestion to cited answer.
- Emphasize **governance by design**: deterministic retrieval + auditable generation context.
- Demonstrate portability from notebook experimentation to scheduled Databricks jobs.

## Architecture Diagram Placeholder

See `docs/architecture/architecture-overview.md` and update the diagram placeholder at:
- `docs/architecture/architecture-diagram-placeholder.drawio`

## Next Steps

- Swap in enterprise vector/search backends (Databricks Vector Search, OpenSearch, etc.).
- Add MLflow tracing and quality benchmarks.
- Introduce CI/CD promotion gates by environment (dev/staging/prod).
