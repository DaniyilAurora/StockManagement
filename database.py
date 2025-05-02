import sqlite3


class Database():
    # Initialise database
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.cursor = self.connection.cursor()

        # Ensure tables exist
        if self.is_first_launch():
            self.create_tables()

    def create_tables(self):
        # Create tables in the database

        # Create "stocks" table
        self.cursor.execute("""
                CREATE TABLE stocks(
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(255),
                    price REAL,
                    image_path VARCHAR(255),
                    is_in_stock BOOLEAN
                );
        """)

        self.connection.commit()

        # Create "accounts" table
        self.cursor.execute("""
                CREATE TABLE accounts(
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255),
                    password BLOB
                );
        """)

        self.connection.commit()

        # Create "sessions" table
        self.cursor.execute("""
                CREATE TABLE sessions(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    token TEXT,
                    expires_at DATETIME
                );
        """)

        self.connection.commit()

    def is_first_launch(self) -> bool:
        # Check for first launch of an app (if table "stocks" exist)
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?;
        """, ("stocks",))

        result = self.cursor.fetchone()

        return result is None
