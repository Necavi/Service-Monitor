from service_monitor.service_base import ServiceBase
from requests import get, ConnectionError


class AsteriskService(ServiceBase):
    type = "HTTP"

    def get_status(self):
        try:
            return get("http://{}".format(self.address)).status_code == 200
        except ConnectionError:
            return False
