"""
Property of Austin Lidey, drafted for CSCD-429 DATA MINING
Created: July 27th, 2022 @ 9:00pm PST

This file consists of the driving code that executes the
homework assignment.
"""
import pandas as pd
from file_processing import import_data_file

data_file_paths = [
    "./gene_files/Genes_relation.data",
    # "./gene_files/Genes_relation.names", # Data may not be needed for processing
    "./gene_files/Genes_relation.test",
    "./gene_files/Interactions_relation.data",
    # "./gene_files/Interactions_relation.names", # Data may not be needed for processing
    "./gene_files/Interactions_relation.test"]

for data_file in data_file_paths:
    print("-----------------------------------------------")
    print(f"{data_file}\n{import_data_file(data_file)}")
