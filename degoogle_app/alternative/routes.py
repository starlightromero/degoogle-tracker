"""Alternative routes."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from degoogle_app.models import Alternative
from degoogle_app import db

alternative = Blueprint("alternative", __name__)


@login_required
@alternative.route("/", methods=["GET"])
def get_alternative_services():
    """Get current user's alternative services."""
    form = AlternativeForm()
    return render_template("alternative.html.j2", form=form)


@login_required
@alternative.route("/", methods=["POST"])
def add_alternative_services():
    """Add new alternative service to current user."""
    form = AlternativeForm()
    if form.validate_on_submit:
        alternative = Alternative(name=form.name.data)
        db.session.add(alternative)
        db.session.commit()
        flash("The alternative service has been added")
    return redirect(url_for("alternative.get_alternative_services"))


@login_required
@alternative.route("/:id", methods=["PATCH"])
def update_alternative_services(id):
    """Update alternative service for current user."""
    alternative = Alternative.query.get_or_404(id)
    form = AlternativeForm()
    if form.validate_on_submit:
        alternative.name = form.name.data
        db.session.commit()
        flash("The alternative service has been updated.")
    return redirect(url_for("alternative.get_alternative_services"))


@login_required
@alternative.route("/:id", methods=["DELETE"])
def delete_alternative_services(id):
    """Delete alternative service for current user."""
    alternative = Alternative.query.get_or_404(id)
    db.session.delete(alternative)
    db.session.commit()
    flash(f"{alternative.name} has been deleted.")
    return redirect(url_for("alternative.get_alternative_services"))
