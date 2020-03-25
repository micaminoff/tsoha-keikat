from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    if form.validate():
        user = User.query.filter_by(
            email=form.email.data, password=form.password.data).first()

        if user:
            login_user(user)
            print("User " + user.email + " signed in")
            return redirect(url_for("events_index"))

    return render_template("auth/loginform.html", form=form,
                           error="Invalid credentials")


@app.route("/auth/create", methods=["POST"])
def auth_create():
    form = LoginForm(request.form)

    if form.validate():
        user = User.query.filter_by(
            email=form.email.data).first()
        if user:
            return render_template("auth/loginform.html", form=form,
                                   error="This email is already in use.")
        u = User(email=form.email.data, password=form.password.data)
        db.session.add(u)
        db.session.commit()
        login_user(u)
        return redirect(url_for('events_index'))

    return render_template("auth/loginform.html", form=form,
                           error="Invalid information")


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("events_index"))
