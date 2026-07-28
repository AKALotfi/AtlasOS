from connection import get_connection

conn = get_connection()

print("SQLite database connected!")

conn.close()