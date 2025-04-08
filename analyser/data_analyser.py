class DataAnalyser:

    def __init__(self, data: list):
        self.data_to_analyse: list = data
        self.clean_data()


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
            number_of_words += len(str(one_line).split(' '))
        return number_of_words