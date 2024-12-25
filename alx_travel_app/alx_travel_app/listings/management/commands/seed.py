import sqlite3

def populate_database():
    with sqlite3.connect('sqlite3.db') as conn:
        cursor = conn.cursor()
        cursor.execute