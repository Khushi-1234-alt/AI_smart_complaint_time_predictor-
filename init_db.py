import sqlite3

conn = sqlite3.connect('ticket_db.db')
cursor = conn.cursor()

# Create complaints table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_text TEXT,
    predicted_category TEXT,
    predicted_time INTEGER
)
""")

# Create feedback table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    complaint TEXT NOT NULL,
    rating INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("✅ Tables created successfully.")
