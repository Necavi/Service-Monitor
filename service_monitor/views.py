from flask import render_template, redirect, url_for

from . import app, services
from .service_monitor import load_monitors


@app.route("/")
def index():
    return render_template("status.html", services=services)


@app.route("/reload")
def reload():
    load_monitors()
    return redirect(url_for("index"))
