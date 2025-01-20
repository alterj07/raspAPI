import sqlite3

def init_db():
    conn = qlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users''')