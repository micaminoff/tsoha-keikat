from application import app, db
from flask import redirect, render_template, request, url_for

from application.events.models import Event
from application.events.forms import EventForm


@app.route("/events", methods=["GET"])
def events_index():
    return render_template("events/list.html", events=Event.query.all())


@app.route("/events/new/")
def event_form():
    return render_template("events/new.html", form=EventForm())


@app.route("/events/", methods=["POST"])
def events_create():
    form = EventForm(request.form)

    e = Event(name=form.name.data,
              performer=form.performer.data,
              venue=form.venue.data,
              date=form.date.data)
    db.session().add(e)
    db.session().commit()
    return redirect(url_for("events_index"))


@app.route("/events/<event_id>/", methods=["GET"])
def events_modify(event_id):
    return render_template("events/modify.html",
                           event=Event.query.get(event_id),
                           form=EventForm())


@app.route("/events/<event_id>/", methods=["POST"])
def events_update(event_id):
    form = EventForm(request.form)

    e = Event.query.get(event_id)

    e.name = form.name.data
    e.performer = form.performer.data
    e.venue = form.venue.data
    e.date = form.date.data

    db.session().commit()

    return redirect(url_for("events_index"))
