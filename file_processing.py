"""
Property of Austin Lidey, drafted for CSCD-429 DATA MINING
Created: July 30th, 2022 @ 12:00pm PST 

This class will handle processing of the input data files 
for the assignment.
"""
import pandas as pd
from colors import t_colors


def import_data_files(user_file_args: list) -> list:
    """Collects all valid data files specified in argv.
        Params:
            user_file_args: List of user specified paths to data files to process.
        Returns:
            list containing pd.DataFrame for each valid data file.
    """
    valid_data_files = []

    for file_path in user_file_args:
        data_file = import_data_file(file_path)
        if data_file is None:
            print(
                f"   {t_colors.FAIL}[FAILURE]{t_colors.ENDC} The file: {file_path} could not be located, skipping...")
        else:
            print(
                f"   {t_colors.OKCYAN}[SUCCESS]{t_colors.ENDC} {file_path} is loaded.")
            valid_data_files.append(data_file)

    return valid_data_files


def import_data_file(file_path: str) -> pd.DataFrame:
    """Reads in data from a CSV file.
        Params:
            file_path: A string representing a single file path
        Returns:
            pd.DataFrame containing raw data from data file.
        Throws:
            FileNotFoundError: When a file cannot be found from path provided.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return None
