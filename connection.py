import sqlite3


class Connection():
    # Initialise connection
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.cursor = self.connection.cursor()

    # Add a new record to the stocks
    def add_record(self, name: str, category: str, quantity: str, price: float):
        self.cursor.execute("""
            INSERT INTO stocks
            (name, category, quantity, price)
            VALUES (?, ?, ?, ?);
        """, (name, category, quantity, price))
        self.connection.commit()

    # Removes a record from the stocks
    def remove_record(self, id: int):
        self.cursor.execute("""
            DELETE FROM stocks WHERE id=?;
        """, (id,))
        self.connection.commit()

    # Returns stocks records
    def get_records(self):
        self.cursor.execute("""
            SELECT * FROM stocks;
        """)

        stocks = self.cursor.fetchall()

        return stocks

    # Closes the connection
    def close(self):
        self.connection.close()
