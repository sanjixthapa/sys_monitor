# database.py
import sqlite3
from config import DB_NAME

def init_db():
    """Initialize the SQLite database and create the table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            cpu_usage REAL,
            memory_usage REAL,
            disk_usage REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_metrics(cpu, mem, disk):
    """Insert system metrics into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO stats (cpu_usage, memory_usage, disk_usage)
        VALUES (?, ?, ?)
    ''', (cpu, mem, disk))
    conn.commit()
    conn.close()

def get_latest_metrics(limit=20):
    """Fetch the latest N metrics for the dashboard."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Access columns by name
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stats ORDER BY id DESC LIMIT ?', (limit,))
    data = cursor.fetchall()
    conn.close()
    return data