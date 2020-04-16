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
        performers = [(performer.id, performer.name)
                      for performer in Performer.query.all()]
        for sub_form in form.performers:
            sub_form.performer.choices = performers

        if not form.validate_on_submit():
            return render_template('events/new.html', form=form)

        for entry in form.performers.entries:
            print(entry.data['performer'])
        performer_ids = [(entry.data['performer'])
                         for entry in form.performers.entries]
        print(performer_ids)
        e = Event(name=form.name.data,
                  performers=[(Performer.query.get(id))
                              for id in performer_ids],
                  venue=form.venue.data,
                  date=form.date.data)
        e.account_id = current_user.id
        db.session().add(e)
        db.session().commit()
        # Then redirect to list of events
        return redirect(url_for("events_index"))

    # GET: Serve form for event creation
    performers = [(performer.id, performer.name)
                  for performer in Performer.query.all()]
    form = EventForm()
    for sub_form in form.performers:
        sub_form.performer.choices = performers
    return render_template("events/new.html", form=form, performers=performers)


@app.route("/events/<event_id>/", methods=["GET", 'POST'])
@login_required
def events_modify(event_id):
    e = Event.query.get(event_id)
    if e.account.id is not current_user.id and not current_user.admin:
        return redirect(url_for('events_index'))

    # POST: Update event
    if request.method == 'POST':
        form = EventForm(request.form)
        performers = [(performer.id, performer.name)
                      for performer in Performer.query.all()]
        for sub_form in form.performers:
            sub_form.performer.choices = performers
        if form.validate():
            performer_ids = [(entry.data['performer'])
                             for entry in form.performers.entries]
            e.name = form.name.data
            e.performers = [(Performer.query.get(id))
                            for id in performer_ids]
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
    performers = [(performer.id, performer.name)
                  for performer in Performer.query.all()]
    iterator = 0
    for sub_form in form.performers:
        sub_form.performer.choices = performers
        sub_form.performer.data = e.performers[iterator].id
        print(e.performers[iterator].id)
        iterator += 1
    return render_template("events/modify.html",
                           form=form, event=e, performers=performers)


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
