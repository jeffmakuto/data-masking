#!/usr/bin/env python3
""" Masked data handling """


class MaskedDataHandler:
    """
    Handles saving masked data
    """
    def __init__(self, loader):
        """
        Initializes a MaskedDataHandler object

        Args:
            loader (DataFrameLoader): An instance of DataFrameLoader
        """
        self.loader = loader

    def save_masked_data(self, output_file: str) -> None:
        """
        Saves masked data frame to a CSV file

        Args:
            output_file (str): Path to output CSV file
        """
        self.loader.df.to_csv(output_file, index=False)
        print(f"Masked data has been saved to {output_file}")
