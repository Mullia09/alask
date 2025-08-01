import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "volunteers.db"

SCHEMA = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        age INTEGER,
        location TEXT,
        community TEXT,
        role TEXT DEFAULT 'participant',
        verified INTEGER DEFAULT 0,
        otp_code TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS programs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        program_id INTEGER NOT NULL,
        check_in TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(program_id) REFERENCES programs(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS reflections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        program_id INTEGER NOT NULL,
        text TEXT,
        sentiment TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(program_id) REFERENCES programs(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS badges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name TEXT,
        description TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS audit_trail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """
]


def connect(path: Path = DB_PATH):
    return sqlite3.connect(path)


def init_db(path: Path = DB_PATH):
    conn = connect(path)
    cur = conn.cursor()
    for statement in SCHEMA:
        cur.execute(statement)
    conn.commit()
    conn.close()

