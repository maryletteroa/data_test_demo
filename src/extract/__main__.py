# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-10-24 14:26:29
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-10-29 12:03:13

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from _includes.paths import data_urls, source_data_dir
from extract.extract_from_urls import get_data_from_urls, write_table_csv

from glob import glob


# extract data tables from source urls
# and write as csv

if not os.path.exists(source_data_dir):
    os.mkdir(source_data_dir)

for name, url in data_urls.items():
    print(f"getting data for: {name}...")
    write_table_csv(
        table = get_data_from_urls(url),
        output_dir = f"{source_data_dir}",
        prefix = name
    )