class DataAnalyser:
    """
    A class for analyzing text-based data from a list of strings.
    The class provides functionality to count lines, words, letters, and identify the most frequent words in the data.
    It performs initial cleaning of the data by removing newlines, tabs, and extra whitespace.

    Attributes:
        data_to_analyse (list): A cleaned list of strings ready for analysis.
    """

    def __init__(self, data: list):
        """
        Initializes the DataAnalyser with raw data.

        Args:
            data (list): A list of strings to be analyzed.
        """
        self._data_to_analyse: list = self._clean_data(data)


    @property
    def data_to_analyse(self) -> list:
        """
        Getter for data_to_analyse

        Returns:
            list: A list of lines from the read file
        """
        return self._data_to_analyse


    @data_to_analyse.setter
    def data_to_analyse(self, new_data: list):
        """
        Setter for data_to_analyse

        Args:
             new_data (list): A list of strings to be analysed.
        """
        self._data_to_analyse = new_data


    @staticmethod
    def _clean_data(data: list) -> list:
        """
        Cleans a list of strings by removing newlines, tabs, and surrounding whitespace.

        Args:
            data (list): A list of raw strings.

        Returns:
            list: A list of cleaned strings.
        """
        cleaned_list = [
            line.replace('\n', '').replace('\t', '').strip()
            for line in data
        ]
        return cleaned_list


    def amount_of_lines(self) -> int:
        """
        Calculates the number of lines in the cleaned data.

        Returns:
            int: The number of lines.
        """
        return len(self.data_to_analyse)


    def amount_of_words(self) -> int:
        """
        Calculates the total number of words across all lines.

        Returns:
            int: The total number of words.
        """
        number_of_words: int = 0
        for one_line in self.data_to_analyse:
            number_of_words += len(one_line.split())
        return number_of_words


    def show_five_most_frequent_words(self) -> list:
        """
        Finds the five most frequently occurring words in the data.

        Returns:
            list: A list of tuples (word, frequency), sorted by frequency in descending order.
        """
        counted_words: dict = DataAnalyser._number_of_occurrences_of_each_word(self.data_to_analyse)
        sorted_words: list = DataAnalyser._sort_items(counted_words)
        return sorted_words


    @staticmethod
    def _number_of_occurrences_of_each_word(source: list) -> dict:
        """
        Counts the number of occurrences of each word in a list of strings.

        Args:
            source (list): A list of cleaned strings.

        Returns:
            dict: A dictionary where keys are words and values are their frequencies.
        """
        counted_words: dict = {}
        for line in source:
            words: list = line.split()
            for word in words:
                if word in counted_words:
                    counted_words[word] += 1
                else:
                    counted_words[word] = 1
        return counted_words


    @staticmethod
    def _sort_items(data: dict) -> list:
        """
        Sorts dictionary items by their values in descending order and returns the top five.

        Args:
            data (dict): A dictionary of word counts.

        Returns:
            list: A list of the top five (word, frequency) tuples.
        """
        sorted_words: list = sorted(data.items(), key = lambda item: item[1], reverse = True)
        return sorted_words[:5]


    def amount_of_letters(self) -> int:
        """
        Calculates the total number of letters in the data, ignoring spaces.

        Returns:
            int: The total number of letters.
        """
        return sum(len(''.join(line.split())) for line in self.data_to_analyse)
