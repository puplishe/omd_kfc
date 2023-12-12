import sqlite3


def dbinit():
    conn = sqlite3.connect('kfc_restaurants.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kfc_locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        address TEXT,
        longitude REAL,
        latitude REAL,
        breakfast_start TEXT,
        breakfast_end TEXT,
        open_time TEXT,
        closed_time TEXT
    )
    ''')
    conn.commit()
    conn.close()


def connection(database='kfc_restaurants.db'):
    conn = sqlite3.connect(database)
    return conn
