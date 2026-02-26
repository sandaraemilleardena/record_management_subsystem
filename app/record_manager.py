class RecordManager:
    def __init__(self):
        self.records = []

    def add_record(self, name):
        from app.record_validator import validate_name

        if not validate_name(name):
            return False

        self.records.append(name)
        return True

    def delete_record(self, name):
        if name in self.records:
            self.records.remove(name)
            return True
        return False

    def search_record(self, name):
        if name in self.records:
            return name
        return None