"""
This .py includes the function that manages files
"""

import pandas as pd
import pathlib
import json
import os
import sys

def file_management_existence(file_catalog_input):
    if not pathlib.Path(file_catalog_input).is_file():
        raise FileNotFoundError("File not found: ", file_catalog_input)

    print("Found file:", file_catalog_input)

def open_file(file_name_input : str, resource : str):
    PATH = "../resources/"
    FULL_PATH = PATH + file_name_input
    file_management_existence(FULL_PATH)

    if resource == "hotel":

        df_columns = ["hotel_id", "name", "location", "rooms_total",
                        "rooms_available", "price_per_night", "rating"]
    
    elif resource == "customer":

        df_columns = ["customer_id", "name", "email", "phone"]

    elif resource == "reservations":

        df_columns = ["hotel_id", "client_id", "reservation_id", "status"]

    try:
        df = pd.read_json(FULL_PATH)

        if df.empty == True:
            raise ValueError()

        return df
    
    except (ValueError, json.JSONDecodeError):
        print("Error: JSON file is corrupted. Using an empty DataFrame.")
        return pd.DataFrame(columns = df_columns)


def save_file(df_input : pd.DataFrame, file_name_input : str):
    PATH = "../resources/"
    FULL_PATH = PATH + file_name_input
    file_management_existence(FULL_PATH)
    df_input.to_json(FULL_PATH, orient="records", indent=4)


def parse_to(df_input : pd.DataFrame, column_name : str, data_type):
    df_input[column_name] = df_input[column_name].astype(data_type)


def empty_check(df_input : pd.DataFrame):
    if df_input.empty:
        print("Error: No hotels found in the database.")
        return False

def check_if_id_exists(resource : str, value_to_search : str):
    try:
        df = open_file(resource + "s.json", resource)
        empty_check(df)

        parse_to(df, resource + "_id", str)

        return value_to_search in df[resource + "_id"].values

    except Exception as e:
        print(f"An error occured: {e}")
        return False

