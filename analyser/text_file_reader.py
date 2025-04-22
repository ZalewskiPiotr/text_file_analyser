from charset_normalizer import from_path
from analyser.logger import logger as global_logger

class TextFileReader:
    """
        A simple utility class to read the contents of a text file.

        Attributes:
            local_logger (analyser.logger): A file logger
            file_path (str): The path to the text file.
            file_contents (list): A list storing lines read from the file.
        """

    def __init__(self, file_path: str):
        """
        Initializes the TextFileReader with the given file path.

        Args:
            file_path (str): Path to the text file.
        """
        self.local_logger = global_logger.getChild(self.__class__.__name__)
        self.local_logger.info(f"Reading the file: {file_path}")

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
            encoding = self._detect_encoding(self.file_path)
            self.local_logger.info(f"Detected an encoding: {encoding}")
            with open(self.file_path, "r+t", encoding=encoding) as file:
                self.file_contents = file.readlines()
        except FileNotFoundError:
                print(f"Error: File '{self.file_path}' not found.")
                self.local_logger.error(f"Error: File '{self.file_path}' not found.")
        except IOError as e:
            print(f"Error reading file '{self.file_path}': {e}")
            self.local_logger.error(f"Error reading file '{self.file_path}': {e}")


    def get_file_content(self) -> list:
        """
        Returns the contents of the file.

        Returns:
            list: A list of lines read from the file.
        """
        return self.file_contents


    @staticmethod
    def _detect_encoding(file_path: str) -> str:
        """
        Detect the encoding of the given file

        Args:
            file_path (str): Path to the file to be read.

        Returns:
            str: The string indicating the type of encoding in a file

        Raises:
            ValueError: If the encoding could not be determined.
        """
        results = from_path(file_path)
        best = results.best()
        if best is None:
            raise ValueError(f"Could not detect encoding for file: {file_path}")
        return best.encoding