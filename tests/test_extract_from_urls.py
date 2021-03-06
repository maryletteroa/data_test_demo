# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-10-24 14:27:58
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-11-11 09:57:13

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import datatest as dt
from datatest import (
    accepted,
    Extra
    )
import pandas as pd
import pytest
from glob import glob
from collections import namedtuple

from src.extract.extract_from_urls import *
from src._includes.paths import data_urls, source_data_dir

# functions that return data tables
# to be used in succeeding tests

def test_exceptions_are_working():
    invalid_url = "www.google.com"
    with pytest.raises(Exception):
        get_data_from_urls("invalid_url")

def test_write_table_csv(tmpdir):
    df = get_data_from_urls(data_urls["stores"])
    write_table_csv(df.head(), tmpdir, "test")
    data_file = f"{tmpdir}/test.csv"
    assert os.path.exists(data_file)

def test_write_table_csv_2(tmpdir):
    df = get_data_from_urls(data_urls["stores"])
    write_table_csv(df.head(), tmpdir, "test")
    data_file = f"{tmpdir}/test.csv"
    assert os.path.exists(data_file)

def test_store_data_columns(store_data):
    with open(store_data) as s_d:
        assert s_d.readlines()[0] == "Store,Type,Size\n"

def test_store_data_columns_2(store_data):
    with open(store_data) as s_d:
        assert s_d.readlines()[0] == "Store,Type,Size\n"

@pytest.fixture
def csvs():
    return (
            f"{source_data_dir}/stores.csv",
            f"{source_data_dir}/sales.csv",
            f"{source_data_dir}/features.csv",
    )

@pytest.fixture
def datasets(csvs):
    Data = namedtuple("Data", ("stores", "sales", "features"))
    data = Data(
            stores = pd.read_csv(csvs[0]),
            sales = pd.read_csv(csvs[1]),
            features = pd.read_csv(csvs[2])
            )
    return data


@pytest.mark.skipif(
    glob(f"{source_data_dir}/*") == [],
    reason="The data has not been extracted yet",
)
class TestFilesExist:
    def test_source_data_dir_exists(self):
        assert os.path.exists(source_data_dir)

    def test_extracted_data(self, csvs):

        # extracted data exists in directory
        for csv in csvs:
            assert os.path.exists(csv)

        # no other file present in folder
        assert set(glob(f"{source_data_dir}/*")) == set(csvs)


# ---------- data testing----------------
@pytest.mark.skipif(
    glob(f"{source_data_dir}/*") == [],
    reason="The data has not been extracted yet",
)
class TestData:
    def test_shapes(self, datasets):
        shapes = {
            "stores" : (45, 3),
            "sales" : (10000, 5),
            "features" : (8190, 8),
        }

        for name, shape in shapes.items():
            dt.validate(getattr(datasets, name).shape, shape)

    def test_column_names(self, datasets):
        required_column_names = {
            "stores": {"Store", "Type", "Size"},
            "sales": {"Store", "Dept", "Date", "Weekly_Sales"},
            "features": {"Fuel_Price", "Date", "Unemployment", 
                "Store", "Temperature", "IsHoliday", "CPI", "MarkDown"},
        }

        for name, cols in required_column_names.items():
            with accepted([
                Extra("IsHoliday"),
            ]):
                dt.validate(getattr(datasets, name).columns, cols)

    def test_data_types(self, datasets):
        dt.validate(datasets.stores, (int, str, int))
        dt.validate(datasets.sales,(int, int, str, float, bool))
        dt.validate(datasets.features, (int, str, *[float]*5, bool))


# --------- expectation suite testing ------------- #
