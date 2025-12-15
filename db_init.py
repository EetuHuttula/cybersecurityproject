#!/usr/bin/env python3
import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def create_tables(db_path=None):
    """Create users and notes tables and insert sample users with hashed passwords."""
    if db_path is None:
        db_path = DB_PATH
    db = sqlite3.connect(db_path)
    db.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK (role IN ('admin','basic'))
    );
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        note TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)
    
    admin_hash = generate_password_hash('admin123')
    basic_hash = generate_password_hash('basic123')
    
    db.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
               ('admin', admin_hash, 'admin'))
    db.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
               ('basic', basic_hash, 'basic'))
    
    db.commit()
    db.close()
    return f"Initialized database at {db_path}"

if __name__ == "__main__":
    print(create_tables())
