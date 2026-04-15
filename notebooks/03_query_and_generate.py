# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - Query and Generate

# COMMAND ----------

from adr_rag_databricks.databricks import build_pipeline, query_pipeline

ADR_DATA_PATH = "/Workspace/Repos/<user>/Learn-Path/sample_adrs"
pipeline = build_pipeline(data_path=ADR_DATA_PATH)
pipeline.index_adr_directory(namespace="adr_prod")

query = "Which ADRs affect risk governance and model validation controls?"
answer = query_pipeline(pipeline, query=query, namespace="adr_prod", include_sources=True, max_context_chunks=5)
print(answer)
