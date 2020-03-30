from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.performers.models import Performer
from application.performers.forms import PerformerForm


@app.route('/performers/')
def performers_index():
    return render_template("performers/list.html",
                           performers=Performer.query.all(),
                           user=current_user)


@app.route("/performers/new/", methods=['GET', 'POST'])
@login_required
def performers_create():
    # POST: Create new performer
    if request.method == 'POST':
        form = PerformerForm(request.form)

        if not form.validate():
            return render_template('performers/new.html', form=form)

        p = Performer(name=form.name.data, genre=form.name.data)
        p.account_id = current_user.id
        db.session().add(p)
        db.session().commit()
        # Then redirect to list of performers
        return redirect(url_for("performers_index"))

    # GET: Serve form for performer creation
    return render_template("performers/new.html", form=PerformerForm())


@app.route('/performers/<performer_id>/', methods=['GET', 'POST'])
def performers_inspect(performer_id):
    p = Performer.query.get(performer_id)
    return render_template('performers/view.html', performer=p, events=[])


@app.route('/performers/modify/<performer_id>/', methods=['GET', 'POST'])
@login_required
def performers_modify(performer_id):
    p = Performer.query.get(performer_id)
    if p.account.id is not current_user.id and not current_user.admin:
        return redirect(url_for('events_index'))

    # POST: Update Performer
    if request.method == 'POST':
        form = PerformerForm(request.form)
        if form.validate():
            p.name = form.name.data
            p.genre = form.genre.data

            db.session().commit()
            # Then redirect to list of events
            return redirect(url_for("performers_index"))
        # If not valid, return to modification form
        return render_template("performers/modify.html",
                               form=form, performer=p)

    # GET: Serve form for event modification
    form = PerformerForm(obj=p)
    return render_template("performers/modify.html",
                           form=form, performer=p)


@app.route("/performers/<performer_id>/delete", methods=["GET", "POST"])
@login_required
def performers_delete(performer_id):
    p = Performer.query.get(performer_id)
    if p.account.id is not current_user.id and not current_user.admin:
        return redirect(url_for('performers_index'))

    # DELETE: Delete event
    if request.method == 'POST':
        print('got a delete request')
        db.session.delete(p)
        db.session.commit()
        return redirect(url_for('performers_index'))

    # GET: Serve form for confirmation
    return render_template('performers/deletion_confirmation.html',
                           performer=p)
