from contextlib import contextmanager
from io import TextIOWrapper


class TempFileWriter:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> TextIOWrapper:
        print(f"Connecting to {self.filename}...")
        self.file = open(self.filename, "w")
        return self.file
    
    def __exit__(self, exc_type, exc, tb):
        print("Closing the connection.")
        if self.file:
            self.file.close()

with TempFileWriter("test.txt") as f:
    f.write("Hello!")


@contextmanager
def temp_file_writer(filename: str):
    print(f"Connecting to {filename}...")
    f = open(filename, "w")
    try: 
        yield f
    except TypeError as e:
        print(f"type error: {e}")
    finally:
        print("Closing the connection.")
        f.close()
    
with temp_file_writer("test2.txt") as f:
    f.write("Hello!")