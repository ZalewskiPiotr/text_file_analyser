class DataAnalyser:

    def __init__(self, data: list):
        self.data_to_analyse: list = data
        self.clean_data()


    def clean_data(self):
        for i in range(len(self.data_to_analyse)):
            line: str = self.data_to_analyse[i]
            line = line.replace('\n', '')
            line = line.replace('\t', '')
            line = line.strip()
            self.data_to_analyse[i] = line


    def amount_of_lines(self) -> int:
        return len(self.data_to_analyse)