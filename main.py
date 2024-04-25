#!/usr/bin/env python3
""" Main script """
from load_csv import DataFrameLoader
from process_data import process_data
from masked import MaskedDataHandler
from data_mask import DataMasker


def main() -> None:
    """
    creating the dataframe from loaded csv
    """
    # Read the content of 'data.txt' and assign it to the variable 'csv_data'
    with open('data.txt', 'r') as file:
        csv_data = file.read()

    # Load CSV data and process it
    output_file = "output.csv"
    process_data(csv_data, output_file)

    # Load CSV data again to mask email addresses
    loader = DataFrameLoader()
    loader.load_csv(csv_data)

    # Mask email addresses
    data_mask = DataMasker(loader)
    data_mask.mask_email_address()

    # Save the masked data to a new file
    masked_output_file = "masked.csv"
    masked_data = MaskedDataHandler(loader)
    masked_data.save_masked_data(masked_output_file)


if __name__ == "__main__":
    main()
