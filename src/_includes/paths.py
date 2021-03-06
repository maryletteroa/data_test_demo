# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-10-20 17:14:05
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-10-29 11:49:19

"""
Contains shared variables
"""

# higher level directories
root_dir = "/mnt/d/Projects/data_tests_demo/retail_data"
scripts_dir = f"{root_dir}/src"
docs_dir = f"{root_dir}/docs"

# data dirs
data_dir = f"{root_dir}/data"
source_data_dir = f"{data_dir}/0_source"
raw_data_dir = f"{data_dir}/1_raw"
clean_data_dir = f"{data_dir}/2_clean"
present_data_dir = f"{data_dir}/3_present"

# profile dirs
data_profile_dir = f"{docs_dir}/data_profiles"
source_data_profile_dir = f"{data_profile_dir}/0_source"
raw_data_profile_dir = f"{data_profile_dir}/1_raw"
clean_data_profile_dir = f"{data_profile_dir}/2_clean"
present_data_profile_dir = f"{data_profile_dir}/3_present"


# great_expectations
great_expectations_root = f"{docs_dir}/great_expectations"
expectations_suite_dir = f"{great_expectations_root}/expectations"


# web urls containing data
data_urls = {
    "stores" : "https://docs.google.com/spreadsheets/d/e/2PACX-1vTuxA2NrdhAi9DDjDdOznMR1fnv1LiUhf2ztG0QqHAgc_gYK9log0XBZv0VjBB4zzFmGN0gzhD63B07/pubhtml",
    "sales": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRxhXER2cpZpyHf1q4Icfc7pT1WrNUR12EZvwa2FHGwuSzzgGr8uIbrtm5jyemvb6HMbfLO9JxUGgLn/pubhtml",
    "features": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvWZRXlB3GMeJRnJQnylZK1G6JFH4oAg8dnNPuQITB0KHZIFO-6ku1hud6zFct3IoNpHINtY_XAiIY/pubhtml"
}