import pytest
from solution.repository.csv_accessor import CsvFileAccessor

def test_read_non_existent_file(tmp_path):
    file_path = tmp_path / "does_not_exist.csv"
    accessor = CsvFileAccessor(file_path, ["A", "B"])
    result = accessor.reading()
    assert result == []

        
def test_save_and_read_back_integrity(tmp_path):
    file_path = tmp_path / "test_budget.csv"
    headers = ["id", "amount", "category"]
    accessor = CsvFileAccessor(file_path, headers)
    data_to_save = [
        {"id": "1", "amount": "100.50", "category": "Food"},
        {"id": "2", "amount": "20.00", "category": "Transport"}
    ]
    accessor.writing(data_to_save) 
    result = accessor.reading()
    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[0]["category"] == "Food"
    assert result[1]["amount"] == "20.00"
    assert list(result[0].keys()) == headers