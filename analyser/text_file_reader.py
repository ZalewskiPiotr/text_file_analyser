class TextFileReader:

    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.file_contents: list = []


    def read_file(self):
        file = open(self.file_path, "r+t")
        for line in file:
            self.file_contents.append(line)
        file.close()

    def get_file_content(self):
        return self.file_contents