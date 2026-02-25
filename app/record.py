class Record:
    def __init__(self, record_id: int, name: str, age: int):
        self.record_id = record_id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Record(ID={self.record_id}, Name={self.name}, Age={self.age})"