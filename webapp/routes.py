from webapp import app
from flask import render_template, flash, redirect, url_for, request
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

    # Cancel
    if form.cancel.data == True:
        return redirect('/index')

    if form.validate_on_submit():

        # flash('Add task: {} with duedate: {}'.format(form.description_task.data, form.duedate_for_task.data))
        # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)

        if form.action_for_task.data == "friends":
            # '/addtask?action=friends'
            return redirect(url_for('addtask', action = form.action_for_task.data))
            # return redirect('/addtask/friends')
        elif form.action_for_task.data == "followers":
            return redirect(url_for('addtask', action = form.action_for_task.data))

    return render_template('AddTask.html', title = 'Add new task', form=form)


@app.route('/addtask/action', methods=['GET', 'POST'])
def friends(action):
    # userform('friends')
    form = UserForm()
    # conn = datastorage.init()

    # Cancel
    if form.cancel.data == True:
        return redirect('/index')

    if form.validate_on_submit():

        if form.user_id.data:
            flash('Add task for id: {}, action: {}'.format(form.user_id.data, 'friends'))
            # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)
            return redirect('/index')

        elif form.screen_name.data:
            flash('Add task for screen name: {}, action: {}'.format(form.screen_name.data, 'friends'))
            # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)
            return redirect('/index')

    return render_template('UserForm.html', title='User ID or Screen name', form=form)

# @app.route('/addtask/followers', methods=['GET', 'POST'])
# def followers():
#     userform('followers')


def userform(action):

    form = UserForm()
    # conn = datastorage.init()

    # Cancel
    if form.cancel.data == True:
        return redirect('/index')

    if form.validate_on_submit():

        if form.user_id.data:
            flash('Add task for id: {}, action: {}'.format(form.user_id.data, action))
            # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)
            return redirect('/index')

        elif form.screen_name.data:
            flash('Add task for screen name: {}, action: {}'.format(form.screen_name.data, action))
            # datastorage.add_task(conn, form.description_task.data, form.duedate_for_task.data)
            return redirect('/index')

    return render_template('UserForm.html', title='User ID or Screen name', form=form)


@app.route('/listtasks')
def listtasks():

    conn = datastorage.init()
    curs = datastorage.read_all_tasks(conn)

    return render_template('ListTasks.html', curs = curs)

