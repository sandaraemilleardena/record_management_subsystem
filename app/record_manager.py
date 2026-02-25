from app.record import Record
from app.record_validator import validate_name


class RecordManager:
    def __init__(self):
        self.records = []

    def add_record(self, name):
        if not validate_name(name):
            return False
        record = Record(name)
        self.records.append(record)
        return True

    def delete_record(self, name):
        for record in self.records:
            if record.name == name:
                self.records.remove(record)
                return True
        return False

    def search_record(self, name):
        for record in self.records:
            if record.name == name:
                return record
        return None