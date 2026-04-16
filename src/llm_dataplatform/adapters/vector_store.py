"""Pluggable vector store adapter interface and in-memory reference implementation."""

import re
from collections import defaultdict

from llm_dataplatform.core.models import ADRChunk, RetrievalResult

_WORD_PATTERN = re.compile(r"[a-zA-Z0-9_]+")


class InMemoryVectorStore:
    """Reference vector store for local tests and notebook demos.

    This class intentionally avoids external dependencies so it can run
    directly inside Databricks notebooks before backend integration.
    """

    def __init__(self) -> None:
        self._index: dict[str, list[ADRChunk]] = defaultdict(list)

    @staticmethod
    def _tokenize(text: str) -> set[str]:
        return {token.lower() for token in _WORD_PATTERN.findall(text)}

    def upsert(self, namespace: str, chunks: list[ADRChunk]) -> int:
        self._index[namespace].extend(chunks)
        return len(chunks)

    def search(self, namespace: str, query: str, top_k: int = 5) -> list[RetrievalResult]:
        candidates = self._index.get(namespace, [])
        query_terms = self._tokenize(query)

        scored: list[RetrievalResult] = []
        for chunk in candidates:
            chunk_terms = self._tokenize(chunk.text)
            overlap = len(query_terms.intersection(chunk_terms))
            if overlap > 0:
                scored.append(RetrievalResult(chunk=chunk, score=float(overlap)))

        return sorted(scored, key=lambda r: r.score, reverse=True)[:top_k]
