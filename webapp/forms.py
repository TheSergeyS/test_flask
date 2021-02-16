from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, InputRequired, ValidationError
import datetime as dt

# https://wtforms.readthedocs.io/en/2.3.x/validators/?highlight=datarequired#wtforms.validators.DataRequired
# def validate_duedate_for_task(form, field):
#     try:
#         duedate_task = dt.datetime.strptime(field.data, "%d.%m.%Y")
#         # All OK
#     except ValueError:
#         raise ValidationError('format Date must be in XX.XX.XXXX format')

class AddTaskForm(FlaskForm):

    description_task = StringField('Description for task', validators=[InputRequired()])
    duedate_for_task = DateField('Due date', format = '%d.%m.%Y', validators=[DataRequired()])
    submit = SubmitField('Add task')

