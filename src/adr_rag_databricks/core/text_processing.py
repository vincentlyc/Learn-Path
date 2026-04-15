"""Text utilities for ADR chunking."""

from adr_rag_databricks.core.models import ADRChunk


class ADRTextChunker:
    """Simple deterministic chunker for ADR markdown text."""

    def __init__(self, chunk_size: int, chunk_overlap: int) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, doc_id: str, title: str, text: str) -> list[ADRChunk]:
        if not text.strip():
            return []

        step = max(1, self.chunk_size - self.chunk_overlap)
        chunks: list[ADRChunk] = []

        for i, start in enumerate(range(0, len(text), step)):
            segment = text[start : start + self.chunk_size].strip()
            if not segment:
                continue
            chunks.append(ADRChunk(doc_id=doc_id, title=title, text=segment, order=i))

        return chunks
