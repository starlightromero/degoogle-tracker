"""Auth routes."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from datetime import date, datetime
from degoogle_app.models import User
from degoogle_app.auth.forms import SignUpForm, LoginForm
from degoogle_app import db

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        redirect(url_for("main.home"))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account Created.")
        return redirect(url_for("auth.login"))
    return render_template("signup.html.j2", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page if next_page else url_for("main.home"))
        flash("Login Unsuccessful. Please verify username and password.")
    return render_template("login.html,j2", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
