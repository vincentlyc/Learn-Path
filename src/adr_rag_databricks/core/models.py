"""Domain models for ADR retrieval and generation."""

from dataclasses import dataclass


@dataclass(slots=True)
class ADRChunk:
    """Chunked ADR content with metadata."""

    doc_id: str
    title: str
    text: str
    order: int


@dataclass(slots=True)
class RetrievalResult:
    """Returned result from vector retrieval."""

    chunk: ADRChunk
    score: float
