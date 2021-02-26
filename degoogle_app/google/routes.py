"""Google routes."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from degoogle_app.models import Google
from degoogle_app import db

google = Blueprint("google", __name__)


@login_required
@google.route("/", methods=["GET"])
def get_google_services():
    """Get current user's google services."""
    form = GoogleForm()
    return render_template("google.html.j2", form=form)


@login_required
@google.route("/", methods=["POST"])
def add_google_services():
    """Add new google service to current user."""
    form = GoogleForm()
    if form.validate_on_submit:
        google = Google(name=form.name.data)
        db.session.add(google)
        db.session.commit()
        flash("The google service has been added.")
    return redirect(url_for("google.get_google_services"))


@login_required
@google.route("/:id", methods=["PATCH"])
def update_google_services(id):
    """Update google service for current user."""
    google = Google.query.get_or_404(id)
    form = GoogleForm()
    if form.validate_on_submit:
        google.name = form.name.data
        db.session.commit()
        flash("The google service has been updated.")
    return redirect(url_for("google.get_google_services"))


@login_required
@google.route("/:id", methods=["DELETE"])
def delete_google_services(id):
    """Delete google service for current user."""
    google = Google.query.get_or_404(id)
    db.session.delete(google)
    db.session.commit()
    flash(f"{google.name} has been deleted.")
    return redirect(url_for("google.get_google_services"))
