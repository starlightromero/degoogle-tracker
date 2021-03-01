"""Alternative routes."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from degoogle_app.alternative.forms import AlternativeForm
from degoogle_app.models import Alternative, Google
from degoogle_app import db

alternative = Blueprint("alternative", __name__)


@alternative.route("/", methods=["GET"])
@login_required
def get_alternative_software():
    """Get current user's alternative software."""
    form = AlternativeForm()
    return render_template("alternative.html.j2", form=form)


@alternative.route("/", methods=["POST"])
@login_required
def add_alternative_software():
    """Add new alternative software to current user."""
    form = AlternativeForm()
    if form.validate_on_submit:
        alternative = Alternative(
            name=form.name.data,
            user_id=current_user.id,
            google_id=form.alternative.data.id,
        )
        db.session.add(alternative)
        db.session.commit()
        flash("The alternative software has been added")
    return redirect(url_for("alternative.get_alternative_software"))


@alternative.route("/<software_id>", methods=["DELETE"])
@login_required
def delete_alternative_software(software_id):
    """Delete alternative software for current user."""
    alternative = Alternative.query.get_or_404(software_id)
    db.session.delete(alternative)
    db.session.commit()
    flash(f"{alternative.name} has been deleted.")
    return redirect(url_for("alternative.get_alternative_software"))
