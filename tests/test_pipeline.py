from pathlib import Path

from adr_rag_databricks.core.config import PipelineConfig
from adr_rag_databricks.pipelines.adr_rag_pipeline import ADRRAGPipeline


def test_pipeline_indexes_and_answers(tmp_path: Path) -> None:
    adr_file = tmp_path / "adr_001_security_controls.md"
    adr_file.write_text(
        "Adopt policy-driven access controls for model deployment and monitoring.",
        encoding="utf-8",
    )

    pipeline = ADRRAGPipeline(config=PipelineConfig(data_path=str(tmp_path)))
    chunk_count = pipeline.index_adr_directory(namespace="test")

    assert chunk_count > 0

    answer = pipeline.answer("What ADR covers model deployment controls?", namespace="test")
    assert "Sources:" in answer
