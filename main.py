#!/usr/bin/env python3
""" Main script """
from load_csv import DataFrameLoader
from process_data import process_data


def main() -> None:
    """
    creating the dataframe from loaded csv
    """
    # Read the content of 'data.txt' and assign it to the variable 'csv_data'
    with open('data.txt', 'r') as file:
        csv_data = file.read()

    output_file = "output.csv"
    process_data(csv_data, output_file)


if __name__ == "__main__":
    main()
