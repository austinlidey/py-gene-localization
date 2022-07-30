"""
Property of Austin Lidey, drafted for CSCD-429 DATA MINING
Created: July 27th, 2022 @ 9:00pm PST

This file consists of the driving code that executes the
homework assignment.
"""
import os
import sys
import pandas as pd
from file_processing import import_data_files

# Flow of Program:
# - Import data files
# -- Prep data files
# --- Apply classifying algorithm
# ---- Collect data generated
# ----- Display data above


def process_input_files(arg_list: list) -> list:
    """Reads user arguments for file paths, and creates list"""
    processed_arg_list = []
    for arg in enumerate(arg_list):
        processed_arg_list.append(arg[1])
    # Remove the file execution arg
    processed_arg_list.reverse()
    processed_arg_list.pop()

    return processed_arg_list


def main():
    """Driver for data processing and execution"""

    # Process arguments for paths
    print("LOADING INPUT FILES...")
    user_file_args = process_input_files(sys.argv)

    # Acquire valid files from paths
    print("PROCESSING INPUT FILES...")
    data_files = import_data_files(user_file_args)


if __name__ == "__main__":
    os.system('color')
    main()
