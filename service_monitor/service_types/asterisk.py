from service_monitor.service_base import ServiceBase


class AsteriskService(ServiceBase):
    type = "Asterisk"

    def get_status(self):
        return True
