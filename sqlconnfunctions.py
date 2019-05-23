from sqlite3 import Error
import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect("test.db")
        return conn
    except Error as e:
        print(e)
 
    return None

def select_all_tasks(conn, id):
    cur = conn.cursor()
    query = "SELECT * FROM uslvi where ID="+str(id)
    cur.execute(query)
    result = cur.fetchall()
    return result

def get_all_columnnames(conn):
    cur = conn.cursor()
    cur.execute('PRAGMA TABLE_INFO({})'.format('uslvi'))
    names = [tup[1] for tup in cur.fetchall()]
    return names
