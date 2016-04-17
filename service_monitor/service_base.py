class ServiceBase(object):
    type = "Base"

    def __init__(self, name, address, options=None):
        self.name = name
        if address == "auto":
            self.address = self._resolve_auto_address
        else:
            self.address = address
        self.options = options if options is not None else {}

    def get_status(self):
        raise NotImplementedError

    def _resolve_auto_address(self):
        raise NotImplementedError


