from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species")
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])



