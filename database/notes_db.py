from database.connection import get_connection


def create_note(title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO notes (title, content)
        VALUES (?, ?)
    """, (title, content))

    conn.commit()
    conn.close()


def get_notes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_notes, title, content, created_at
        FROM notes
    """)

    notes = cursor.fetchall()

    conn.close()

    return notes


def get_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_notes, title, content, created_at
        FROM notes
        WHERE id_notes = ?
    """, (note_id,))

    note = cursor.fetchone()

    conn.close()

    return note


def update_note(note_id, title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE notes
        SET title = ?, content = ?
        WHERE id_notes = ?
    """, (title, content, note_id))

    conn.commit()
    conn.close()


def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM notes
        WHERE id_notes = ?
    """, (note_id,))

    conn.commit()
    conn.close()