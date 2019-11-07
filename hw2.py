""" Create a python module which can read url and test dataframe """
import pandas as pd


def read_function(url):
    """ reads creates a dataframe from a URL that points to a CSV file"""
    df = pd.read_csv(url)
    return df


def test_create_dataframe(df, column_names):
    """
    Test if the DataFrame contains only the columns that you specified as the second argument.
    Test if the values in each column have the same python type
    Test if there are at least 10 rows in the DataFrame.
    :param df:
    :param column_names:
    :return: true of false
    """
    # The DataFrame contains only the columns that you specified as the second argument.
    df_column_names = df.columns.tolist()
    set_df_column = set(df_column_names)
    set_column = set(column_names)
    if set_df_column != set_column:
        return False
    # The values in each column have the same python type
    for i in range(len(list(df.dtypes))):
        for j in range(list(df.count())[i]):
            if type(df.iloc[j, i]) != type(df.iloc[0, i]):
                return False
    # There are at least 10 rows in the DataFrame.
    if df.shape[0] < 10:
        return False
    return True
