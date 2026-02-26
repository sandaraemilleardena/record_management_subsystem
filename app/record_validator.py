def validate_id(record_id):
    if record_id is None:
        return False
    if not isinstance(record_id, int):
        return False
    return True


def validate_name(name):
    if not isinstance(name, str):
        return False
    if not name.strip():
        return False
    return True


def validate_age(age):
    if not isinstance(age, int):
        return False
    if age < 0:
        return False
    return True