from database.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    #Table of notes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id_notes INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP           
        )
    """)

    conn.commit()
    conn.close()