from mcstatus import MinecraftServer

from service_monitor.service_base import ServiceBase


class MinecraftService(ServiceBase):
    type = "Minecraft"

    def __init__(self, name, address, options=None):
        super().__init__(name, address, options)
        self.server = MinecraftServer.lookup(self.address)

    def get_status(self):
        try:
            self.server.status()
            return True
        except OSError as e:
            print(e)
            return False

    def details(self):
        details = super().details()
        info = self.server.status()
        details.update({
            "Max Players": info.players.max,
            "Online Players": info.players.online,
            "Description": info.description
        })
        return details
