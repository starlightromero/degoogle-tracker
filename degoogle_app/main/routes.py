"""Main routes."""
from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Home template."""
    return render_template("home.html.j2")
