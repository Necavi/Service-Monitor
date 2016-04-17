from . import app, services


@app.route("/")
def index():
    return "<br>".join(["{} ({}): {}".format(service.name, service.type, service.get_status()) for service in services])
