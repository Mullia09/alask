import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import os
import sqlite3
from volunteer_app.db import init_db, DB_PATH


def test_init_db(tmp_path):
    db_file = tmp_path / "test.db"
    init_db(db_file)
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cur.fetchall()}
    expected = {
        'users',
        'programs',
        'attendance',
        'reflections',
        'badges',
        'audit_trail'
    }
    assert expected.issubset(tables)
    conn.close()


