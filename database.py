import sqlite3
from contextlib import closing
from config import DB_PATH

def init_db():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, telegram_id INTEGER UNIQUE, username TEXT, role TEXT DEFAULT 'client')''')
            conn.execute('''CREATE TABLE IF NOT EXISTS leads(id	INTEGER PRIMARY KEY AUTOINCREMENT, client_id INTEGER, manager_id INTEGER, description TEXT, status TEXT DEFAULT 'new')''')

init_db()

def add_user(telegram_id, username):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)''', (telegram_id, username))

def add_user_lead(description, client_id):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''INSERT INTO leads (description, client_id) VALUES (?, ?)''', (description, client_id))
            return conn.lastrowid

def role_manager(user_id, role):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''UPDATE users SET role = ? WHERE telegram_id = ?''', (role, user_id))

def get_leads():
    with closing(sqlite3.connect(DB_PATH)) as conn:
            return conn.execute('''SELECT id, description FROM leads WHERE status = ? ORDER BY id''', ('new',)).fetchall()

def get_leads_in_process():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        return conn.execute('''SELECT id, description FROM leads WHERE status = ? ORDER BY id''', ('in_process',)).fetchall()

def get_leads_ready():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        return conn.execute('''SELECT id, description FROM leads WHERE status = ? ORDER BY id''', ('closed',)).fetchall()

def get_from_leads(lead_id):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        row = conn.execute('''SELECT client_id FROM leads WHERE id = ?''', (lead_id,)).fetchone()
        if row is None:
            return None
        return row[0]

def update_status_manager_leads(status, manager_id, id_leads):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''UPDATE leads SET status = ?, manager_id = ? WHERE id = ?''',  (status, manager_id, id_leads))

def get_stats():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            rows = conn.execute('''SELECT status, COUNT(*) FROM leads GROUP BY status''').fetchall()
            stats = {'new': 0, 'in_progress': 0, 'closed': 0}
            for status, count in rows:
                stats[status] = count
            stats['total'] = sum(stats.values())
            return stats