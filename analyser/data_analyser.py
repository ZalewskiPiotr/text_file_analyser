class DataAnalyser:

    def __init__(self, data: list):
        self.data_to_analyse: list = self.clean_data(data)


    def clean_data(self, data: list) -> list:
        cleaned_list = [
            line.replace('\n', '').replace('\t', '').strip()
            for line in data
        ]
        return cleaned_list


    def amount_of_lines(self) -> int:
        return len(self.data_to_analyse)


    def amount_of_words(self) -> int:
        number_of_words: int = 0
        for one_line in self.data_to_analyse:
            number_of_words += len(one_line.split())
        return number_of_words


    def show_five_most_frequent_words(self) -> list:
        counted_words: dict = self.number_of_occurrences_of_each_word(self.data_to_analyse)
        sorted_words: list = self.sort_items(counted_words)
        return sorted_words


    def number_of_occurrences_of_each_word(self, source: list) -> dict:
        counted_words: dict = {}
        for line in source:
            words: list = line.split()
            for word in words:
                if word in counted_words:
                    counted_words[word] += 1
                else:
                    counted_words[word] = 1
        return counted_words


    def sort_items(self, data: dict) -> list:
        sorted_words: list = sorted(data.items(), key = lambda item: item[1], reverse = True)
        return sorted_words[:5]


    def amount_of_letters(self) -> int:
        return sum(len(''.join(line.split())) for line in self.data_to_analyse)
