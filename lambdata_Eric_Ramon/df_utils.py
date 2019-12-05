"""
utility functions for working with DataFrames
"""

import pandas as pd
from sklearn.model_selection import train_test_split

TEST_DF = pd.DataFrame([1, 2, 3, 4, 5, 6])


def train_val_test_split(df, target):
    """
    takes a dataframe and a target (column name), and returns
    X_train, y_train, X_val, y_val, X_test, y_test (in that order)
    """
    X_tv, X_test, y_tv, y_test = train_test_split(df, df[target],
                                                  test_size=0.15,
                                                  random_state=42)

    X_train, X_val, y_train, y_val = train_test_split(X_tv, y_tv,
                                                      test_size=0.2,
                                                      random_state=42)

    return X_train, y_train, X_val, y_val, X_test, y_test


def null_check(df):
    """
    Goes through a dataframe by column, reports total null values
    found in each column, and returns total null values found in
    DataFrame
    """
    totalnull = 0
    nulls = 0

    for column in df:
        nulls = df[column].isnull().sum()
        if nulls > 0:
            print('{} total nulls in {}'.format(nulls, column))
            totalnull += nulls

    return totalnull
