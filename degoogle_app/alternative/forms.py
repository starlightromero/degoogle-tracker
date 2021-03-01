"""Alternative forms."""
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from degoogle_app.models import Google


class AlternativeForm(FlaskForm):
    name = StringField(
        "Alternative Software",
        validators=[DataRequired(), Length(min=3, max=50)],
    )
    alternative = QuerySelectField(
        "Alternative To",
        query_factory=lambda: Google.query.filter(
            Google.user_id == current_user.id
        ).order_by(Google.name),
        allow_blank=False,
        validators=[DataRequired()],
    )
    submit = SubmitField("Add")
