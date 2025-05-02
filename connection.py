import sqlite3


class Connection():
    def __init__(self):
        self.connection = sqlite3.connect("db.db")
        self.cursor = self.connection.cursor()

    def add_record(self, name: str, price: float, image_path: str, is_in_stock: bool):
        self.cursor.execute("""
            INSERT INTO stocks
            (name, price, image_path, is_in_stock)
            VALUES (?, ?, ?, ?);
        """, (name, price, image_path, is_in_stock))
        self.connection.commit()

    def get_records(self):
        self.cursor.execute("""
            SELECT * FROM stocks;
        """)

        stocks = self.cursor.fetchall()

        return stocks

    def close(self):
        self.connection.close()
