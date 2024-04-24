#!/usr/bin/env python3
""" Loading a csv """
from io import StringIO
from typing import Optional
try:
    import pandas as pd
except ImportError:
    pd = None


Class DataFrameLoader:
    """
    class to load CSV data
    """
    def __init__(self) -> None:
        """
        Initializes a DataFrameLoader object
        """
        self.df: Optional[pd.DataFrame] = None

    def load_csv(self, csv_data: str) -> None:
        """
        loads csv data into the dataframe

        Args:
            csv_data (str): CSV data as a string

        Returns:
            None
        """
        if pd is None:
            raise ImportError("pandas library is required to load CSV data.")
        self.df = pd.read_csv(StringIO(csv_data))
