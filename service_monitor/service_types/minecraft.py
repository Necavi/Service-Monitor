from time import time

from mcstatus import MinecraftServer

from service_monitor.service_base import ServiceBase

colours = {
    "0": "000000",
    "1": "0000AA",
    "2": "00AA00",
    "3": "00AAAA",
    "4": "AA0000",
    "5": "AA00AA",
    "6": "FFAA00",
    "7": "AAAAAA",
    "8": "555555",
    "9": "5555FF",
    "a": "55FF55",
    "b": "55FFFF",
    "c": "FF5555",
    "d": "FF55FF",
    "e": "FFFF55",
    "f": "FFFFFF"
}


def colourize(buff):
    reading_colour = False
    in_colour = False
    out = "<span class='outline'>"
    for char in buff:
        if char == "§":
            reading_colour = True
        elif reading_colour:
            if char in colours.keys():
                if in_colour:
                    out += "</span>"
                out += "<span style='color: #{}'>".format(colours[char])
                in_colour = True
            reading_colour = False
        else:
            out += char
    if in_colour:
        out += "</span>"
    out += "</span>"
    return out


class MinecraftService(ServiceBase):
    type = "Minecraft"

    def __init__(self, name, address, options=None):
        super().__init__(name, address, options)
        self.server = MinecraftServer.lookup(self.address)
        self.next_query = 0
        self.info = None

    def get_status(self):
        return self._get_server_info() is not None

    def details(self):
        details = super().details()
        info = self._get_server_info()
        if info is not None:
            details.update({
                "Max Players": info.players.max,
                "Online Players": info.players.online,
                "Description": colourize(info.description.replace("\n", "<br>")),
                "Favicon": "<img src='{}' />".format(info.favicon)
            })
        return details

    def _get_server_info(self):
        if self.next_query > time():
            return self.info
        try:
            self.info = self.server.status()
        except OSError:
            self.info = None
        self.next_query = time() + 15
        return self.info
