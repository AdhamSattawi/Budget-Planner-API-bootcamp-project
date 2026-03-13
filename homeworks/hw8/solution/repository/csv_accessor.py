import csv
from typing import Sequence

class CsvFileAccessor:
    def __init__(self, file_path: str, field_names: Sequence[str]) -> None:
        self.file_path = file_path
        self.field_names = field_names

    def reading(self) -> list[dict]:
        try:
            with open(self.file_path, "r") as file:
                csvfile = csv.DictReader(file)
                return list(csvfile)

        except FileNotFoundError:
            return []

    def writing(self, data: list[dict]) -> None:
        try:
            with open(self.file_path, "w", newline="") as file:
                csvfile = csv.DictWriter(file, self.field_names)
                csvfile.writeheader()
                csvfile.writerows(data)

        except Exception as error:
            raise CsvWritingError(
                "[Error] something went wrong with writing on the csv."
            ) from error


class CsvWritingError(Exception):
    """Raise when there is a problem with writing on the csv file."""
