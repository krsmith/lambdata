""" lambdata - a Data Science Helper
"""
import numpy as np
import pandas as pd

# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
#   This is not an in_place update to the dataframe,
#   must set dataframe = ymd_columns()


def ymd_columns(dataframe, column_name):
    dataframe = df.copy()
    dataframe[column_name] = pd.to_datetime(dataframe[column_name])
    dataframe['Year'] = dataframe[column_name].dt.year
    dataframe['Month'] = dataframe[column_name].dt.month
    dataframe['Day'] = dataframe[column_name].dt.day
    return dataframe

# Function to add column with just year & month
#   This is not an in_place update to the dataframe,
#   must set dataframe = ym_column()


def ym_column(dataframe, column_name):
    dataframe['yearMonth'] = dataframe[column_name].dt.to_period('M')
    return dataframe

# Single function to take a list, turn it into a series and add it to
# a dataframe as a new column
#   This is not an in_place update to the dataframe,
#   must set dataframe = list_to_column()


def list_to_column(dataframe, list, column_name):
    dataframe[column_name] = pd.Series(l, index=dataframe.index)
    return dataframe.head()

# Function to return any row from a dataframe that has a NaN in any column


def null_in_row(dataframe):
    dataframe[dataframe.isnull().any(axis=1)]
