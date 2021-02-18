from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, InputRequired, ValidationError
import datetime as dt

# https://wtforms.readthedocs.io/en/2.3.x/validators/?highlight=datarequired#wtforms.validators.DataRequired
# def validate_duedate_for_task(form, field):
#     try:
#         duedate_task = dt.datetime.strptime(field.data, "%d.%m.%Y")
#         # All OK
#     except ValueError:
#         raise ValidationError('format Date must be in XX.XX.XXXX format')

def action_for_task():

    choices = []
    # Getting All Friends or Followers for a User
    choices.append(('Friends',   'Friends'))
    choices.append(('Followers', 'Followers'))
    # Analyzing a User’s Favorite Tweets
    choices.append(('favorite_tw', 'User’s Favorite Tweets'))

    return choices

class AddTaskForm(FlaskForm):

    # description_task = StringField('Description for task', validators=[InputRequired()])
    # duedate_for_task = DateField('Due date', format = '%d.%m.%Y', validators=[DataRequired()])
    action_for_task = SelectField('Action', choices = action_for_task(), validate_choice = True)

    next = SubmitField('Next')
    cancel = SubmitField('Cancel')

class UserForm(FlaskForm):

    # description_task = StringField('Description for task', validators=[InputRequired()])
    # duedate_for_task = DateField('Due date', format = '%d.%m.%Y', validators=[DataRequired()])
    # action_for_task = SelectField('Action', choices = action_for_task(), validate_choice = True)

    user_id     = StringField('user id', validators=[InputRequired()])
    screen_name = StringField('screen name', validators=[InputRequired()])

    next        = SubmitField('Next')
    cancel      = SubmitField('Cancel')
