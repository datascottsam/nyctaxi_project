# Databricks notebook source
spark.sql("create catalog if not exists nyctaxi managed location 'abfss://unity-catalog-storage@dbstorageqbwv575vawrvc.dfs.core.windows.net/7405609251355798'")

# COMMAND ----------

spark.sql("create schema if not exists nyctaxi.00_landing")
spark.sql("create schema if not exists nyctaxi.01_bronze")
spark.sql("create schema if not exists nyctaxi.02_silver")
spark.sql("create schema if not exists nyctaxi.03_gold")


# COMMAND ----------

spark.sql("create volume if not exists nyctaxi.00_landing.data_source")

# COMMAND ----------

