from flask import render_template, redirect, url_for

from . import app, services
from .service_monitor import load_monitors


@app.route("/")
def index():
    return render_template("status.html", services=
    [(service, service.get_status(), service.details()) for service in sorted(services, key=lambda x: x.name)])


@app.route("/reload")
def reload_config():
    load_monitors()
    return redirect(url_for("index"))
