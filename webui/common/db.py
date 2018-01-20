""" Database lib """
import sqlite3


def connect_db():
    """ Connect to database"""
    rv = sqlite3.connect('/tmp/users.db')
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """ Get DB"""
    database = connect_db()
    return database

def init_db():
    db = get_db()
    with open('/Users/midiblack/Desktop/home-projects/docker-web-ui/schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# init_db()

def add_entry():
    db = get_db()
    fields = ['alx', 'alx@yandex.ru', 'P@ssw0rd']
    db.execute('insert into users (username, email, password) values (?,?,?)', fields)
    db.commit()

add_entry()

def show_entries():
    db = get_db()
    cur = db.execute('select username, id, email, password from users')
    entries = cur.fetchall()
    return entries

for k,v,e, p in show_entries():
    print(k,v,e,p)
