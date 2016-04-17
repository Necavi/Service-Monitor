import os
import inspect

from configobj import ConfigObj
from pluginbase import PluginBase

from . import app
from .exceptions import TypeNotFoundError
from .service_base import ServiceBase


services = set()
service_types = dict()

service_type_loader = PluginBase(package="service_monitor.service_types")
service_type_source = service_type_loader.make_plugin_source(
    searchpath=[os.path.join(os.path.dirname(os.path.abspath(__file__)), "service_types")], persist=True)


def load_types():
    service_types.clear()
    for service_type in service_type_source.list_plugins():
        plugin = service_type_source.load_plugin(service_type)
        for name, cls in inspect.getmembers(plugin):
            if inspect.isclass(cls) and issubclass(cls, ServiceBase) and cls is not ServiceBase:
                service_types[cls.type] = cls


def load_monitors():
    if os.path.exists("./service_monitor/services.cfg"):
        services.clear()
        cfg = ConfigObj("./service_monitor/services.cfg")
        for name, service in cfg.items():
            if service["type"] in service_types:
                services.add(service_types[service["type"]](name, service["address"]))
            else:
                raise TypeNotFoundError(name, service["type"])


def run(*args, **kwargs):
    load_types()
    load_monitors()
    app.run(*args, **kwargs)

