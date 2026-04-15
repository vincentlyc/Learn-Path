"""Helpers to keep pipeline usage straightforward in Databricks notebooks."""

from adr_rag_databricks.core.config import PipelineConfig, QueryConfig
from adr_rag_databricks.pipelines.adr_rag_pipeline import ADRRAGPipeline


def build_pipeline(data_path: str, chunk_size: int = 600, chunk_overlap: int = 80, top_k: int = 5) -> ADRRAGPipeline:
    """Factory utility for notebook-first usage."""
    config = PipelineConfig(
        data_path=data_path,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        top_k=top_k,
    )
    return ADRRAGPipeline(config=config)


def query_pipeline(
    pipeline: ADRRAGPipeline,
    query: str,
    namespace: str = "default",
    include_sources: bool = True,
    max_context_chunks: int = 5,
) -> str:
    """Notebook-friendly query helper."""
    return pipeline.answer(
        query=query,
        namespace=namespace,
        query_config=QueryConfig(include_sources=include_sources, max_context_chunks=max_context_chunks),
    )
