from flask import Flask

app = Flask(__name__)

from .service_monitor import run, services

from . import views


