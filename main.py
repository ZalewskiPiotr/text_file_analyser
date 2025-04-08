from analyser import text_file_reader as txt_reader
from analyser.data_analyser import DataAnalyser

if __name__ == "__main__":
    file_path = "data/the_last_ember.txt"
    file_reader: txt_reader.TextFileReader = txt_reader.TextFileReader(file_path)
    file_reader.read_file()

    analyser: DataAnalyser = DataAnalyser(file_reader.get_file_content())
    print(analyser.amount_of_lines())
    print(analyser.amount_of_words())