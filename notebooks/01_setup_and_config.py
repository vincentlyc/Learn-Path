# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Setup and Config
# MAGIC
# MAGIC Update `ADR_DATA_PATH` to your mounted workspace path or repo folder.

# COMMAND ----------

ADR_DATA_PATH = "/Workspace/Repos/<user>/Learn-Path/sample_adrs"

# COMMAND ----------

from adr_rag_databricks.databricks import build_pipeline

pipeline = build_pipeline(data_path=ADR_DATA_PATH, chunk_size=600, chunk_overlap=80)
pipeline
