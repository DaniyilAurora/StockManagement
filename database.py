import sqlite3


class Database():
    # Initialise database
    def __init__(self):
        self.connection = sqlite3.connect("db.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        # self.cursor.execute("INSERT INTO accounts VALUES (1, 'admin', '5f4dcc3b5aa765d61d8327deb882cf99')")
        # self.connection.commit()

        # Ensure tables exist
        if self.is_first_launch():
            self.create_tables()

    # Create tables in the database
    def create_tables(self):

        # Create "stocks" table
        self.cursor.execute("""
                CREATE TABLE stocks(
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(255),
                    category VARCHAR(255),
                    quantity INTEGER,
                    price REAL
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

        # Create "stockUpdates" table
        self.cursor.execute("""
                CREATE TABLE stockUpdates(
                    id INTEGER PRIMARY KEY,
                    date DATETIME,
                    updateType VARCHAR(255),
                    name VARCHAR(255),
                    quantity INTEGER,
                    updateInformation TEXT
                );
        """)

        self.connection.commit()

    # Check for first launch of an app (if table "stocks" exist)
    def is_first_launch(self) -> bool:
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?;
        """, ("stocks",))

        result = self.cursor.fetchone()

        return result is None
