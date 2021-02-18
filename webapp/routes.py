from webapp import app
from flask import render_template, flash, redirect
from webapp.forms import AddTaskForm, UserForm
import webapp.datastorage as datastorage

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addtask', methods=['GET', 'POST'])
def addtask():

    form = AddTaskForm()
    # conn = datastorage.init()

    if form.validate_on_submit():

        # flash('Add task: {} with duedate: {}'.format(form.description_task.data, form.duedate_for_task.data))
        # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)

        # Cancel
        if form.cancel.data == True:
            return redirect('/index')

        if form.action_for_task.data == "Friends":
            return redirect('/userform')
        elif form.action_for_task.data == "Followers":
            return redirect('/userform')

    return render_template('AddTask.html', title = 'Add new task', form=form)


@app.route('/userform', methods=['GET', 'POST'])
def userform():

    form = UserForm()
    # conn = datastorage.init()

    if form.validate_on_submit():

        # Cancel
        if form.cancel.data == True:
            return redirect('/index')

        if form.action_for_task.data == "Friends":
            # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)
            return redirect('/userform', form.action_for_task.data)
        elif form.action_for_task.data == "Followers":
            # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)
            return redirect('/userform', form.action_for_task.data)

    return render_template('UserForm.html', title='User ID or Screen name', form=form)


@app.route('/listtasks')
def listtasks():

    conn = datastorage.init()
    curs = datastorage.read_all_tasks(conn)

    return render_template('ListTasks.html', curs = curs)

