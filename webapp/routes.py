from webapp import app
from flask import render_template, flash, redirect
from webapp.forms import AddTaskForm
import webapp.datastorage as datastorage

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/AddTask', methods=['GET', 'POST'])
def AddTask():

    form = AddTaskForm()
    conn = datastorage.init()

    if form.validate_on_submit():

        # flash('Add task: {} with duedate: {}'.format(form.description_task.data, form.duedate_for_task.data))
        datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)
        return redirect('/index')

    return render_template('AddTask.html', title = 'Add new task', form=form)

