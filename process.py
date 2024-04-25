#!/usr/bin/env python3
""" data processing """
from load_csv import DataFrameLoader
from process_data import process_data
from data_mask import DataMasker
from masked import MaskedDataHandler


class DataProcessor:
    """
    class to process the data
    """
    def __init__(self, input_file: str, output_file: str,
                 masked_output_file: str) -> None:
        """
        Initialization

        Args:
            input_file (str): original file containing data
            output_file (str): dataframed data
            masked_output_file (str): masked data
        """
        self.input_file = input_file
        self.output_file = output_file
        self.masked_output_file = masked_output_file

    def process(self) -> None:
        """
        method to process data
        """
        loader = DataFrameLoader()
        with open(self.input_file, 'r') as file:
            csv_data = file.read()

        # Load CSV data and process it
        process_data(csv_data, self.output_file)

        # Load CSV data again to mask email addresses
        loader.load_csv(csv_data)

        # Mask email addresses
        data_masker = DataMasker(loader)
        data_masker.mask_email_address()

        # Save the masked data to a new file
        masked_data = MaskedDataHandler(loader)
        masked_data.save_masked_data(self.masked_output_file)
