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

from analyser import text_file_reader as txt_reader
from analyser.data_analyser import DataAnalyser
from analyser.logger import logger
from analyser import history

if __name__ == "__main__":
    logger.info("********** Starting the programme **********")

    # Read the file
    file_path = "data/the_last_ember.txt"
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