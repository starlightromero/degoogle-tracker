"""Google routes."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from degoogle_app.google.forms import GoogleForm
from degoogle_app.models import Google
from degoogle_app import db

google = Blueprint("google", __name__)


@google.route("/", methods=["GET"])
@login_required
def get_google_software():
    """Get current user's google software."""
    form = GoogleForm()
    return render_template("google.html.j2", form=form)


@google.route("/", methods=["POST"])
@login_required
def add_google_software():
    """Add new google software to current user."""
    form = GoogleForm()
    if form.validate_on_submit:
        google = Google(name=form.name.data, user_id=current_user.id)
        db.session.add(google)
        db.session.commit()
        flash("The google software has been added.")
    return redirect(url_for("google.get_google_software"))


@google.route("/<int:software_id>", methods=["POST"])
@login_required
def delete_google_software(software_id):
    """Delete google software for current user."""
    google = Google.query.get_or_404(software_id)
    db.session.delete(google)
    db.session.commit()
    flash(f"{google.name} has been deleted.")
    return redirect(url_for("google.get_google_software"))
