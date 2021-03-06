# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-10-21 14:44:11
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-10-29 14:26:53

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from _includes.paths import raw_data_dir, source_data_dir
from ingest_data import read_csv_to_spark, write_spark_table
from pyspark.sql import SparkSession

names = ("stores", "sales", "features")

if not os.path.exists(raw_data_dir):
    os.mkdir(raw_data_dir)


for name in names:
    df = read_csv_to_spark(
        csv_file_path = f"{source_data_dir}/{name}.csv",
        tag="new"
    )

    print(f"writing raw table for {name}")

    write_spark_table(
        data = df,
        partition_col = "p_ingest_date",
        output_dir = raw_data_dir,
        name = name,
        mode = "overwrite",
    )
