#!/usr/bin/env python3
""" Main script """
from process import DataProcessor


def main():
    input_file = 'data.txt'
    output_file = 'output.csv'
    masked_output_file = 'masked.csv'

    processor = DataProcessor(input_file, output_file, masked_output_file)
    processor.process()


if __name__ == "__main__":
    main()
    