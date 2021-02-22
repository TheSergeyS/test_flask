from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, InputRequired, ValidationError
import datetime as dt

# https://wtforms.readthedocs.io/en/2.3.x/validators/?highlight=datarequired#wtforms.validators.DataRequired

def action_for_task():

    choices = []
    # Getting All Friends or Followers for a User
    choices.append(('friends',   'Friends'))
    choices.append(('followers', 'Followers'))
    # Analyzing a User’s Favorite Tweets
    choices.append(('favorite_tw', 'User’s Favorite Tweets'))

    return choices

class AddTaskForm(FlaskForm):

    # description_task = StringField('Description for task', validators=[InputRequired()])
    # duedate_for_task = DateField('Due date', format = '%d.%m.%Y', validators=[DataRequired()])
    action_for_task = SelectField('Action', choices = action_for_task(), validate_choice = True)

    next = SubmitField('Next')
    cancel = SubmitField('Cancel')


def my_id_name_check(form, field):
    if not form.screen_name.data and not form.user_id.data:
        raise ValidationError('You must fill in field "screen name" or "userid"')

class UserForm(FlaskForm):

    user_id     = StringField('user id', validators=[my_id_name_check])
    screen_name = StringField('screen name', validators=[my_id_name_check])

    next        = SubmitField('Next')
    cancel      = SubmitField('Cancel')
