import json
import os
from datetime import datetime


class History:
    """
    A class for managing the history of file analysis operations.

    This class logs metadata (e.g., line and word count) for analyzed files and saves it to a JSON-formatted
    log file (`history.log` by default).
    """

    def __init__(self):
        """Initializes the History object and sets the default log file path."""
        self.history_file = "history.log"

    def add_entry_to_history(self, number_of_lines: int, number_of_words: int, file_name: str,
                             current_date: datetime = datetime.now().isoformat()) -> None:
        """
        Adds a new entry to the history log.

        Args:
            number_of_lines (int): The number of lines in the analyzed file.
            number_of_words (int): The number of words in the analyzed file.
            file_name (str): The name of the analyzed file.
            current_date (str, optional): The date and time of the analysis
                in ISO format. Defaults to the current timestamp.
        """
        entry = {
            "date_and_time": current_date,
            "number_of_lines": number_of_lines,
            "number_of_words": number_of_words,
            "file_name": file_name
        }

        history: list = self._load_history_file()
        history.append(entry)
        self._save_history_file(entry, history)


    def _load_history_file(self) -> list:
        """
        Loads the history data from the log file.

        Returns:
            list: A list of previous history entries (each as a dictionary).
        """
        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf-8") as file:
                return list(json.load(file))
        else:
            return []


    def _save_history_file(self, entry: dict, history: list) -> None:
        """
        Saves the updated history back to the log file.

        Args:
            entry (dict): The latest entry to be logged.
            history (list): The full list of history entries to be written.
        """
        with open(self.history_file, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)
