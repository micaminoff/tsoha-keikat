from application import app, db
from flask import redirect, render_template, request, url_for
from application.events.models import Event
import datetime


@app.route("/events", methods=["GET"])
def events_index():
    return render_template("events/list.html", events=Event.query.all())


@app.route("/events/new/")
def event_form():
    return render_template("events/new.html")


@app.route("/events/", methods=["POST"])
def events_create():
    data = request.form
    e = Event(name=data.get("name"),
              performer=data.get("performer"),
              venue=data.get("venue"),
              date=datetime.datetime.strptime(data.get("date"), "%Y-%m-%d").date())
    db.session().add(e)
    db.session().commit()
    return redirect(url_for("events_index"))
