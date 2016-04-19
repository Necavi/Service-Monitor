from time import time

from valve.source.a2s import ServerQuerier, NoResponseError

from service_monitor.service_base import ServiceBase


class SrcdsService(ServiceBase):
    type = "srcds"

    def __init__(self, name, address, options=None):
        super().__init__(name, address, options)
        host, _, port = self.address.partition(":")
        port = int(port) if port != "" else 27015
        self.server = ServerQuerier((host, port))
        self.next_query = 0
        self.info = {}

    def get_status(self):
        try:
            return bool(self._get_server_info())
        except ConnectionError:
            return False

    def details(self):
        details = super().details()
        details.update({
            key.replace("_", " "): value for key, value in self._get_server_info().items()
            if key in self.options["query_keys"]
        })
        return details

    def _get_server_info(self):
        if self.next_query > time():
            return self.info
        try:
            self.info = self.server.get_info()
        except (NoResponseError, OSError):
            self.info = {}
        self.next_query = time() + 15
        return self.info
