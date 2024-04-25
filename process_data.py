#!/usr/bin/env python3
""" Process the csv data """
from load_csv import DataFrameLoader


def process_data(csv_data: str, output_file: str) -> None:
    """
    Process the CSV data and save the dataframe to a CSV file.

    Args:
        csv_data (str): CSV data in string format.
        output_file (str): Name of the output CSV file.
    """
    loader = DataFrameLoader()
    loader.load_csv(csv_data)

    loader.df.to_csv(output_file, index=False)
    print(f"Dataframe has been saved to {output_file}")
