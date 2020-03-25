from application import app, db
from flask import redirect, render_template, request, url_for

from application.events.models import Event
from application.events.forms import EventForm


@app.route("/events/")
def events_index():
    return render_template("events/list.html", events=Event.query.all())


@app.route("/events/new/", methods=['GET', 'POST'])
def events_create():
    # POST: Create new event
    if request.method == 'POST':
        form = EventForm(request.form)

        if not form.validate():
            return render_template('events/new.html', form=form)

        e = Event(name=form.name.data,
                  performer=form.performer.data,
                  venue=form.venue.data,
                  date=form.date.data)
        db.session().add(e)
        db.session().commit()
        # Then redirect to list of events
        return redirect(url_for("events_index"))

    # GET: Serve form for event creation
    return render_template("events/new.html", form=EventForm())


@app.route("/events/<event_id>/", methods=["GET", 'POST'])
def events_modify(event_id):
    e = Event.query.get(event_id)

    # POST: Update event
    if request.method == 'POST':
        form = EventForm(request.form)
        if form.validate():
            e.name = form.name.data
            e.performer = form.performer.data
            e.venue = form.venue.data
            e.date = form.date.data

            db.session().commit()
            # Then redirect to list of events
            return redirect(url_for("events_index"))
        return render_template("events/modify.html",
                               form=form, event=e)

    # GET: Serve form for event modification
    form = EventForm(obj=e)
    return render_template("events/modify.html",
                           form=form, event=e)
