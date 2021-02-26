"""Alternative forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from degoogle_app.models import Google


class AlternativeForm(FlaskForm):
    name = StringField(
        "Alternative Service",
        validators=[DataRequired(), Length(min=3, max=50)],
    )
    alternative = QuerySelectField(
        "Alternative To",
        query_factory=lambda: Google.query,
        allow_blank=False,
    )
    submit = SubmitField("Add")
