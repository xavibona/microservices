import sqlite3

DB = 'auth.db'

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
''')
init_db()