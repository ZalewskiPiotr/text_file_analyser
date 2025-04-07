class DataAnalyser:

    def __init__(self, data: list):
        self.data_to_analyse = data

    def amount_of_lines(self) -> int:
        return len(self.data_to_analyse)