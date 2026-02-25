class Record:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

    def update_name(self, new_name):
        if not new_name:
            raise ValueError("New name cannot be empty")
        self.name = new_name