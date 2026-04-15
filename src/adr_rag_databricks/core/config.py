"""Configuration primitives for ADR RAG pipelines."""

from dataclasses import dataclass


@dataclass(slots=True)
class PipelineConfig:
    """Runtime pipeline configuration."""

    data_path: str
    chunk_size: int = 600
    chunk_overlap: int = 80
    top_k: int = 5

    def __post_init__(self) -> None:
        if not (100 <= self.chunk_size <= 4000):
            msg = "chunk_size must be between 100 and 4000"
            raise ValueError(msg)
        if not (0 <= self.chunk_overlap <= 1000):
            msg = "chunk_overlap must be between 0 and 1000"
            raise ValueError(msg)
        if not (1 <= self.top_k <= 20):
            msg = "top_k must be between 1 and 20"
            raise ValueError(msg)


@dataclass(slots=True)
class QueryConfig:
    """Query-time options."""

    include_sources: bool = True
    max_context_chunks: int = 5

    def __post_init__(self) -> None:
        if not (1 <= self.max_context_chunks <= 20):
            msg = "max_context_chunks must be between 1 and 20"
            raise ValueError(msg)
