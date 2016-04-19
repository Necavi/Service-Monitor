class ServiceBase(object):
    type = "Base"

    def __init__(self, name, address, options=None):
        self.name = name
        self.address = address
        self.options = options if options is not None else {}

    def get_status(self):
        raise NotImplementedError

    def details(self):
        return {"Address": self.address}


