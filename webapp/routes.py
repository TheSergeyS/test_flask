from webapp import app
from flask import render_template, flash, redirect
from webapp.forms import AddTaskForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/AddTask', methods=['GET', 'POST'])
def AddTask():
    form = AddTaskForm()
    if form.validate_on_submit():
        flash('Add task: {} with duedate: {}'.format(form.description_task, form.duedate_for_task))
        return redirect('/index')
        # pass
    return render_template('AddTask.html', title = 'Add new task', form=form)

