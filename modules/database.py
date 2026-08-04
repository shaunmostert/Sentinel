import sqlite3


def get_connection():
    return sqlite3.connect("sentinel.db")


def create_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_type TEXT,
            username TEXT,
            source_ip TEXT,
            port INTEGER,
            service TEXT,
            raw_log TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_event(event):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO events
        (
            timestamp,
            event_type,
            username,
            source_ip,
            port,
            service,
            raw_log
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        event["timestamp"],
        event["event_type"],
        event["username"],
        event["source_ip"],
        event["port"],
        event["service"],
        event["raw_log"]
    ))

    connection.commit()
    connection.close()

def get_events():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM events")

    results = cursor.fetchall()

    connection.close()

    return results