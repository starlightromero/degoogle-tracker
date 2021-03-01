"""Google forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class GoogleForm(FlaskForm):
    name = StringField(
        "Google Software", validators=[DataRequired(), Length(min=3, max=50)]
    )
    submit = SubmitField("Add")
