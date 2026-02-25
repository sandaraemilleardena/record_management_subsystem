class RecordValidator:

    @staticmethod
    def validate_id(record_id):
        if record_id is None:
            raise ValueError("ID cannot be None")

        if not isinstance(record_id, int):
            raise ValueError("ID must be integer")

    @staticmethod
    def validate_name(name):
        if not name or name.strip() == "":
            raise ValueError("Name cannot be empty")

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int):
            raise ValueError("Age must be integer")

        if age < 0:
            raise ValueError("Age cannot be negative")