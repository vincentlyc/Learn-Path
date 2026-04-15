# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Index ADR Documents

# COMMAND ----------

from adr_rag_databricks.databricks import build_pipeline

ADR_DATA_PATH = "/Workspace/Repos/<user>/Learn-Path/sample_adrs"
pipeline = build_pipeline(data_path=ADR_DATA_PATH)
indexed_chunks = pipeline.index_adr_directory(namespace="adr_prod")
print(f"Indexed chunks: {indexed_chunks}")
