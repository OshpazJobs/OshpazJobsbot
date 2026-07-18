import sqlite3

db = sqlite3.connect("oshpazjobs.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    full_name TEXT,
    phone TEXT,
    language TEXT,
    role TEXT
)
""")

db.commit()
