from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    # If method is POST, validate form data
    form = LoginForm(request.form)

    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                # Only login if form valid, user exists, and passwords match
                login_user(user)
                print("User " + user.email + " signed in")
                return redirect(url_for("events_index"))

    # If anything in user authentication fails, serve login form with errors
    return render_template("auth/loginform.html", form=form,
                           error="Invalid credentials")


@app.route("/auth/create", methods=["GET", "POST"])
def auth_create():

    if request.method == 'GET':
        return render_template("auth/registerform.html", form=LoginForm())

    # If method is POST, validate form data
    form = LoginForm(request.form)

    if form.validate():
        user = User.query.filter_by(
            email=form.email.data).first()
        if user:
            # Enforce unique emails
            return render_template("auth/loginform.html", form=form,
                                   error="This email is already in use.")

        # If valid email, create user and has password, then login and redirect
        pw_hash = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        u = User(email=form.email.data,
                 password=pw_hash)
        if form.admin.data is True:
            u.admin = True
        db.session.add(u)
        db.session.commit()
        login_user(u)
        print(u)
        return redirect(url_for('events_index'))

    # If anything in POST goes wrong, serve login form with errors
    return render_template("auth/registerform.html", form=form,
                           error="Invalid information")


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("events_index"))
