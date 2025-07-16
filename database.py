import sqlite3
from sqlite3 import Error

DB_NAME = "chat_history.db"

def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            conn.close()
        except Error as e:
            print(f"Error creating table: {e}")

def save_message(role, content):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
            conn.commit()
            conn.close()
        except Error as e:
            print(f"Error saving message: {e}")

def load_messages(limit=50):
    conn = create_connection()
    messages = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", (limit,))
            rows = cursor.fetchall()
            messages = [{"role": row[0], "content": row[1]} for row in reversed(rows)]
            conn.close()
        except Error as e:
            print(f"Error loading messages: {e}")
    return messages
