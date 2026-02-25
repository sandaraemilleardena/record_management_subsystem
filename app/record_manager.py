from app.record import Record
from app.record_validator import RecordValidator


class RecordManager:

    def __init__(self):
        self.records = []

    def add_record(self, record_id, name, age):

        RecordValidator.validate_id(record_id)
        RecordValidator.validate_name(name)
        RecordValidator.validate_age(age)

        if self.search_record(record_id) is not None:
            raise ValueError("Duplicate ID not allowed")

        record = Record(record_id, name, age)

        self.records.append(record)

        return record

    def search_record(self, record_id):

        for record in self.records:
            if record.record_id == record_id:
                return record

        return None

    def delete_record(self, record_id):

        record = self.search_record(record_id)

        if record is None:
            raise ValueError("Record not found")

        self.records.remove(record)

        return True

    def update_record(self, record_id, name, age):

        record = self.search_record(record_id)

        if record is None:
            raise ValueError("Record not found")

        RecordValidator.validate_name(name)
        RecordValidator.validate_age(age)

        record.name = name
        record.age = age

        return record