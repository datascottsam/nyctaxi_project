# Databricks notebook source
import urllib.request
import shutil
import os

# COMMAND ----------


dates_to_process = ['2025-11','2025-12','2026-01','2026-02','2026-03','2026-04']


for date in dates_to_process:

    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{date}.parquet"

    response = urllib.request.urlopen(url)
    dir_path =f"/Volumes/nyctaxi/00_landing/data_source/nyctaxi_yellow/{date}"
    os.makedirs(dir_path,exist_ok=True)

    local_path = f"{dir_path}/yellow_tripdata_{date}.parquet"

    with open(local_path,'wb') as f:
        shutil.copyfileobj(response,f)