"""
Property of Austin Lidey, drafted for CSCD-429 DATA MINING
Created: July 30th, 2022 @ 12:00pm PST 

This file will process the input data files for the assignment.
"""
import pandas as pd


def import_data_file(file_path: str) -> pd.DataFrame:
    """ Reads in data from a CSV file"""
    if file_path is None:
        raise FileNotFoundError
    return pd.read_csv(file_path)
