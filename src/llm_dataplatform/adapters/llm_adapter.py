"""LLM adapter abstraction with deterministic fallback generator."""

from llm_dataplatform.core.models import RetrievalResult


class DeterministicLLMAdapter:
    """Reference LLM adapter for notebook demos.

    Replace this class with a Databricks Model Serving client for production.
    """

    def generate(self, query: str, contexts: list[RetrievalResult], include_sources: bool = True) -> str:
        if not contexts:
            return "No relevant ADR context was found for the query."

        summary = (
            f"Query: {query}\n"
            "Top ADR insights:\n"
            + "\n".join(
                f"- [{i+1}] {result.chunk.title}: {result.chunk.text[:160]}..."
                for i, result in enumerate(contexts)
            )
        )

        if include_sources:
            summary += "\n\nSources: " + ", ".join(
                f"{r.chunk.doc_id}#chunk-{r.chunk.order}" for r in contexts
            )

        return summary
