"""
Main script for analyzing a text file using the DataAnalyser module.

This script reads the contents of a text file, analyzes it, and prints:
- The number of lines
- The number of words
- The number of characters (excluding spaces)
- The five most frequent words

Modules:
    analyser.text_file_reader (as txt_reader): Handles file reading operations.
    analyser.data_analyser: Provides tools for text analysis.

Usage:
    Run this script directly to analyze the file specified by `file_path`.

Example:
    $ python main.py
"""
import argparse

from analyser import text_file_reader as txt_reader
from analyser.data_analyser import DataAnalyser
from analyser.logger import logger
from analyser import history


def get_cli_parameters() -> tuple:
    """
    Parses command-line arguments for file reading options.

    This function sets up an argument parser that accepts parameters for reading a text file directly via a file path
    or using a configuration file. It returns the parsed values as a tuple.

    Returns:
        tuple: A tuple containing:
            - use_config_file (bool): Indicates whether to use a configuration file.
            - file_path (str or None): The path to the file to be read. This is required if `use_config_file` is False.

    Raises:
        SystemExit: If the command-line arguments are improperly formatted or missing required values
        (e.g., if neither `--use_config_file` nor `--file_path` is provided).

    Example:
        To use a config file:
            $ python script.py --use_config_file

        To provide a file path directly:
            $ python script.py --file_path path/to/file.txt
    """
    parser = argparse.ArgumentParser(description="Read text files and show basics information about a content",
                                     epilog='Made by PiotrZET')
    parser.add_argument("-c", "--use_config_file", action='store_true',
                        help="Specify whether to read information from the config file. If you don't use this parameter, the program needs the parameter '-f'.")
    parser.add_argument("-f", "--file_path", help="The path to the file that have to be read")
    args = parser.parse_args()
    return args.use_config_file, args.file_path


if __name__ == "__main__":
    logger.info("********** Starting the programme **********")

    # Get parameters from CLI
    use_config_file, cli_file_path = get_cli_parameters()

    files_paths = []
    if use_config_file:
        print('Using config file is in progress')
        # TODO: fill the files_paths from config file
    else:
        if cli_file_path is None:
            message: str = "Path is empty. I'm not able to read any file."
            logger.warning(message)
            print(f"WARNING!!!. {message}")
            exit()
        else:
            files_paths.append(cli_file_path)

    # Read the file
    for file_path in files_paths:
        file_reader: txt_reader.TextFileReader = txt_reader.TextFileReader(file_path)
        file_reader.read_file()

        # Analyse the data
        analyser: DataAnalyser = DataAnalyser(file_reader.get_file_content())
        number_of_lines: int = analyser.amount_of_lines()
        number_of_words: int = analyser.amount_of_words()
        number_of_letters: int = analyser.amount_of_letters()
        the_five: list = analyser.show_five_most_frequent_words()

        # Print the results
        print(f"Number of lines in a text file: {number_of_lines}")
        print(f"Number of words in a text file: {number_of_words}")
        print(f"Number of characters in a text file: {number_of_letters}")
        print(f"The five most frequent words in a text file: {the_five}")

        # Save the history
        history = history.History()
        history.add_entry_to_history(number_of_lines = number_of_lines, number_of_words = number_of_letters,
                                     file_name = file_path)

    logger.info("---------- Ending the programme ----------")