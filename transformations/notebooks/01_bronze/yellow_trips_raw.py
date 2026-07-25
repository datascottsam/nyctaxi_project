# Databricks notebook source
import pyspark.sql.functions as F
from dateutil.relativedelta import relativedelta
from datetime import date, datetime, timezone

# COMMAND ----------


# Obtains the year-month for 2 months prior to the current month in yyyy-MM format
two_months_ago = date.today() - relativedelta(months=2)
formatted_date = two_months_ago.strftime("%Y-%m")
print(formatted_date)

df = spark.read.format('parquet').load(f"/Volumes/nyctaxi/00_landing/data_source/nyctaxi_yellow/{str(formatted_date)}")

df.display()

# COMMAND ----------

df = df.withColumn("processed_timestamp",F.current_timestamp())

# COMMAND ----------

df.write.mode('append').saveAsTable("nyctaxi.01_bronze.yellow_trips_raw")

# COMMAND ----------

df.display()

# COMMAND ----------

df.select('payment_type').distinct().display()