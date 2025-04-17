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
        Reads the contents of the file specified by self.file_path.

        Opens the file in read and write text mode ("r+t") and stores its lines in the `self.file_contents` attribute.

        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If an I/O error occurs while reading the file.
        """
        try:
            with open(self.file_path, "r+t") as file:
                self.file_contents = file.readlines()
        except FileNotFoundError:
                print(f"Error: File '{self.file_path}' not found.")
        except IOError as e:
            print(f"Error reading file '{self.file_path}': {e}")


    def get_file_content(self):
        """
        Returns the contents of the file.

        Returns:
            list: A list of lines read from the file.
        """
        return self.file_contents