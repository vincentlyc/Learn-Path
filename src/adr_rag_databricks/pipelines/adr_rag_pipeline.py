"""Main ADR RAG pipeline orchestration."""

from pathlib import Path

from adr_rag_databricks.adapters.llm_adapter import DeterministicLLMAdapter
from adr_rag_databricks.adapters.vector_store import InMemoryVectorStore
from adr_rag_databricks.core.config import PipelineConfig, QueryConfig
from adr_rag_databricks.core.text_processing import ADRTextChunker


class ADRRAGPipeline:
    """High-level pipeline that is notebook-friendly and production-extensible."""

    def __init__(
        self,
        config: PipelineConfig,
        vector_store: InMemoryVectorStore | None = None,
        llm_adapter: DeterministicLLMAdapter | None = None,
    ) -> None:
        self.config = config
        self.chunker = ADRTextChunker(config.chunk_size, config.chunk_overlap)
        self.vector_store = vector_store or InMemoryVectorStore()
        self.llm_adapter = llm_adapter or DeterministicLLMAdapter()

    def index_adr_directory(self, namespace: str = "default") -> int:
        base = Path(self.config.data_path)
        files = sorted(base.glob("*.md"))
        total = 0

        for file in files:
            text = file.read_text(encoding="utf-8")
            chunks = self.chunker.split(doc_id=file.stem, title=file.stem.replace("_", " "), text=text)
            total += self.vector_store.upsert(namespace=namespace, chunks=chunks)

        return total

    def answer(self, query: str, namespace: str = "default", query_config: QueryConfig | None = None) -> str:
        cfg = query_config or QueryConfig()
        contexts = self.vector_store.search(namespace=namespace, query=query, top_k=cfg.max_context_chunks)
        return self.llm_adapter.generate(query=query, contexts=contexts, include_sources=cfg.include_sources)
