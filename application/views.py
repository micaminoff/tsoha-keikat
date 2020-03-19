from flask import redirect, url_for
from application import app


# Just redirect to /events. Saving this for project structure
# and potential landing page
@app.route("/")
def index():
    return redirect(url_for("events_index"))
