def validate_name(name):
    if not isinstance(name, str):
        return False
    if not name.strip():
        return False
    return True