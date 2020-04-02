from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.events.models import Event
from application.events.forms import EventForm
from application.performers.models import Performer


@app.route("/events/")
def events_index():
    return render_template("events/list.html",
                           events=Event.query.all(),
                           user=current_user)


@app.route("/events/new/", methods=['GET', 'POST'])
@login_required
def events_create():
    # POST: Create new event
    if request.method == 'POST':
        form = EventForm(request.form)
        print(form.performer.data)
        # This line... after 4 hours of debugging I finally solved it.
        form.performer.choices = [(performer.id, performer.name) for performer in Performer.query.all()]

        if not form.validate():
            return render_template('events/new.html', form=form)

        e = Event(name=form.name.data,
                  performers=[Performer.query.get(form.performer.data)],
                  venue=form.venue.data,
                  date=form.date.data)
        e.account_id = current_user.id
        db.session().add(e)
        db.session().commit()
        # Then redirect to list of events
        return redirect(url_for("events_index"))

    # GET: Serve form for event creation
    form = EventForm()
    form.performer.choices = [(performer.id, performer.name) for performer in Performer.query.all()]
    return render_template("events/new.html", form=form)


@app.route("/events/<event_id>/", methods=["GET", 'POST'])
@login_required
def events_modify(event_id):
    e = Event.query.get(event_id)
    if e.account.id is not current_user.id and not current_user.admin:
        return redirect(url_for('events_index'))

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
        # If not valid, return to modification form
        return render_template("events/modify.html",
                               form=form, event=e)

    # GET: Serve form for event modification
    form = EventForm(obj=e)
    return render_template("events/modify.html",
                           form=form, event=e)


@app.route("/events/<event_id>/delete", methods=["GET", "POST"])
@login_required
def events_delete(event_id):
    e = Event.query.get(event_id)
    if e.account.id is not current_user.id:
        return redirect(url_for('events_index'))

    # DELETE: Delete event
    if request.method == 'POST':
        print('got a delete request')
        db.session.delete(e)
        db.session.commit()
        return redirect(url_for('events_index'))

    # GET: Serve form for confirmation
    return render_template('events/deletion_confirmation.html', event=e)
