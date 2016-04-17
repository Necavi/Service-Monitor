from service_monitor.service_base import ServiceBase
from requests import get


class AsteriskService(ServiceBase):
    type = "HTTP"

    def get_status(self):
        return get("http://{}/".format(self.address)).status_code == 200

    def _resolve_auto_address(self):
        pass
