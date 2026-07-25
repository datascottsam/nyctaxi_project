# Databricks notebook source
import pyspark.sql.functions as F
import pyspark.sql.types as T

# COMMAND ----------

df = spark.read.format('csv').option('header',True).load("/Volumes/nyctaxi/00_landing/data_source/lookup/taxi_zone_lookup.csv")

# COMMAND ----------

df = df.select(
        F.col("LocationID").cast(T.IntegerType()).alias('location_id'),
        F.col("Borough").alias('borough'),
        F.col("Zone").alias("zone"),
        F.col('service_zone'),
        F.current_timestamp().alias('effective_date'),
        F.lit(None).cast(T.TimestampType()).alias('end_date')
)

# COMMAND ----------

df.write.mode('overwrite').saveAsTable('nyctaxi.02_silver.taxi_zone_lookup')