from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    description_task = StringField('Description for task')
    # duedate_for_task = DateField('Due date', validators=[DataRequired()])
    duedate_for_task = StringField('Due date')
    submit = SubmitField('Add task')