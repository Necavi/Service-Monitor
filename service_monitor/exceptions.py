class TypeNotFoundError(Exception):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return """Service type "{}" required by service monitor "{}" not found.""".format(self.type, self.name)
