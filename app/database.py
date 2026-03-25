import sqlite3

def init_db():
    conn = sqlite3.connect('feedback.db')
    conn.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, name TEXT, message TEXT)")
    conn.close()