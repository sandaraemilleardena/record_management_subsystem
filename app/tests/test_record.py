import pytest
from app.record import Record
from app.record_validator import validate_name
from app.record_manager import RecordManager


# 1
def test_record_creation():
    record = Record("Dara")
    assert record.name == "Dara"


# 2
def test_record_creation_empty():
    with pytest.raises(ValueError):
        Record("")


# 3
def test_update_name():
    record = Record("Dara")
    record.update_name("James")
    assert record.name == "James"


# 4
def test_validate_name_cases():
    assert validate_name("Dara") is True
    assert validate_name("") is False
    assert validate_name("   ") is False
    assert validate_name(123) is False


# 5
def test_add_record_success():
    manager = RecordManager()
    assert manager.add_record("Dara") is True
    assert len(manager.records) == 1


# 6
def test_add_record_invalid():
    manager = RecordManager()
    assert manager.add_record("") is False
    assert len(manager.records) == 0


# 7
def test_delete_record():
    manager = RecordManager()
    manager.add_record("Dara")
    assert manager.delete_record("Dara") is True
    assert len(manager.records) == 0


# 8
def test_search_record():
    manager = RecordManager()
    manager.add_record("Dara")
    assert manager.search_record("Dara") is not None
    assert manager.search_record("James") is None