import sqlite3

db_filename = 'testDB.sqllite'

def init():

    conn = sqlite3.connect(db_filename)
    curs = conn.cursor()
    curs.execute("""
            CREATE TABLE IF NOT EXISTS "TaskQueue" (
              id INTEGER PRIMARY KEY,
              Description TEXT,
              _is_done boolean default FALSE,
              _is_deleted boolean default FALSE,
              CreatedOn Date DEFAULT CURRENT_DATE,
              DueDate Date);
              """)

    # curs.execute("""
    #           CREATE TABLE IF NOT EXISTS "InfoAboutTask" (
    #             id INTEGER PRIMARY KEY,
    #             action TEXT,
    #             user_id TEXT,
    #             screen_name TEXT,
    #
    #             _is_done boolean default FALSE,
    #             _is_deleted boolean default FALSE,
    #             CreatedOn Date DEFAULT CURRENT_DATE,
    #             DueDate Date);
    #             """)

    return conn

def add_task(conn, description, duedate):

    # 1.
    cursor = conn.cursor()
    query = """INSERT INTO TaskQueue (Description, DueDate)
                VALUES (:description, :duedate)"""
    cursor.execute(query, {'description': description, 'duedate': duedate})
    conn.commit()

    # 2.
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO TaskQueue (Description, DueDate) VALUES (?, ?)", (description, duedate))
    # conn.commit()

def mark_task_complete(conn, id_task):

    cursor = conn.cursor()
    query = "UPDATE TaskQueue SET _is_done = 'TRUE' WHERE id = :id"
    cursor.execute(query, {'id':id_task})
    conn.commit()

def read_all_tasks(conn):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TaskQueue WHERE _is_done = 'FALSE'")

    return cursor.fetchall()

    # print("[%-2s] [%-20s] [%-10s] [%-10s] [%s]" % ("id", "description", "is_deleted", "createdon", "duedate"))
    # for row in cursor.fetchall():
    #     id, description, _is_done, _is_deleted, createdon, duedate = row
    #     print("{%-2s} %-22s [%-10s] (%-10s) (%s)" % (id, description, _is_deleted, createdon, duedate))
