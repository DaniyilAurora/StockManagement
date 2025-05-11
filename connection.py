import sqlite3
from datetime import datetime


class Connection():
    # Initialise connection
    def __init__(self):
        self.connection = sqlite3.connect("db.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    # Add a new record to the stocks
    def add_record(self, name: str, category: str, quantity: str, price: float):
        # Add record to stocks
        self.cursor.execute("""
            INSERT INTO stocks
            (name, category, quantity, price)
            VALUES (?, ?, ?, ?);
        """, (name, category, quantity, price))
        self.connection.commit()

        # Add log information to stockUpdates
        self.cursor.execute("""
            INSERT INTO stockUpdates
            (date, updateType, name, quantity, updateInformation)
            VALUES (?, ?, ?, ?, ?);
        """, (datetime.now().date(), "Add", name, quantity, "New stock added"))
        self.connection.commit()

    # Removes a record from the stocks
    def remove_record(self, id: int):
        # Get record data
        self.cursor.execute("""
            SELECT * FROM stocks WHERE id=?;
        """, (id,))
        record_data = self.cursor.fetchall()

        # Remove record from stocks
        self.cursor.execute("""
            DELETE FROM stocks WHERE id=?;
        """, (id,))
        self.connection.commit()

        # Add log information to stockUpdates
        print(record_data)
        print(record_data[0][1])
        self.cursor.execute("""
            INSERT INTO stockUpdates
            (date, updateType, name, quantity, updateInformation)
            VALUES (?, ?, ?, ?, ?);
        """, (datetime.now().date(), "Remove", record_data[0][1], -record_data[0][3], "Stock removed"))
        self.connection.commit()

    # Returns stocks records
    def get_records(self):
        self.cursor.execute("""
            SELECT * FROM stocks;
        """)

        stocks = self.cursor.fetchall()

        return stocks

    def get_categories(self):
        self.cursor.execute("""
            SELECT DISTINCT category
            FROM stocks
            ORDER BY category ASC;
        """)

        rows = self.cursor.fetchall()

        # Make a tuple into list of strings
        categories = [row[0] for row in rows]

        return categories

    # Get userID using username and encoded password
    def get_id(self, username: str, password: str):
        self.cursor.execute("""
            SELECT id FROM accounts WHERE username = ? AND password = ?
        """, (username, password))

        result = self.cursor.fetchone()

        # In order to return integer, or None
        return result[0] if result else None

    # Closes the connection
    def close(self):
        self.connection.close()
