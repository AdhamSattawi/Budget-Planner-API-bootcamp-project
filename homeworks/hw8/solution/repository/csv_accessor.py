import csv

class CsvFileAccessor:
    def __init__(self, file_path: str, field_names: list[str]) -> None:
        self.file_path = file_path
        self.field_names = field_names

    def reading(self) -> list[dict]:
        try:
            with open(self.file_path, "r") as f:
                csvfile = csv.DictReader(f)
                return list(csvfile)

        except FileNotFoundError:
            return[]

    def writing(self, data: list[dict]) -> None:
        try:
            with open(self.file_path, "w", newline = "") as f:
                csvfile = csv.DictWriter(f, self.field_names)
                csvfile.writeheader()
                csvfile.writerows(data)

        except Exception as e:
            raise CsvWritingError("[Error] something went wrong with writing on the csv.") from e
            

class CsvWritingError(Exception):
    """Raise when there is a problem with writing on the csv file."""
    pass

