from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateFilmForm(FlaskForm):
    """ form template for adding films """
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    submit= SubmitField('Add Film')


class UpdateFilmForm(FlaskForm):
    """ form template for updating films """
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    submit = SubmitField('Update Film')


class ConfirmDelete(FlaskForm):
    """ form template for deleting films """
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Delete Film')