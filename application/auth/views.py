from flask import render_template, request, redirect, url_for

from application import app
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
            print("User " + user.email + " signed in")
            return redirect(url_for("events_index"))

    return render_template("auth/loginform.html", form=form,
                           error="No such username or password")
