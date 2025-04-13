class TextFileReader:
    """
        A simple utility class to read the contents of a text file.

        Attributes:
            file_path (str): The path to the text file.
            file_contents (list): A list storing lines read from the file.
        """

    def __init__(self, file_path: str):
        """
        Initializes the TextFileReader with the given file path.

        Args:
            file_path (str): Path to the text file.
        """
        self.file_path: str = file_path
        self.file_contents: list = []


    def read_file(self):
        """
        Reads the content of the file line by line and stores it in file_contents.

        Opens the file in read and write mode ("r+t"), reads each line and appends it to the file_contents list.
        """
        file = open(self.file_path, "r+t")
        for line in file:
            self.file_contents.append(line)
        file.close()


    def get_file_content(self):
        """
        Returns the contents of the file.

        Returns:
            list: A list of lines read from the file.
        """
        return self.file_contents