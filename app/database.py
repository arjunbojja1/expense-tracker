import sqlite3

DATABASE = 'expense_tracker.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn
