from flask import Flask, render_template, request, redirect, url_for
from database import Database
from connection import Connection


class App():
    # When app is initialised
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_database()
        self.setup_routes()

    # Setup database for the app
    def setup_database(self):
        self.database = Database()

    # Setup routes for the app
    def setup_routes(self):
        @self.app.route("/")
        def home():
            return "<p>Hello, World!</p>"

        @self.app.route("/db")
        def database_display():
            connection = Connection()
            records = connection.get_records()
            connection.close()

            return render_template("index.html", records=records)

        @self.app.route("/addStock", methods=['POST'])
        def add_stock():
            connection = Connection()

            # TODO: Add checks to input (if not empty etc.)
            name = request.form['name'].strip()
            category = request.form['category'].strip()
            quantity = request.form['quantity'].strip()
            price = request.form['price'].strip()

            if name and category and quantity and price:
                connection.add_record(name, category, quantity, price)
            connection.close()

            return redirect(url_for('database_display'))

        @self.app.route("/removeStock", methods=['POST'])
        def remove_stock():
            connection = Connection()

            # TODO: Add checks to input (if id > 0 etc.)
            id = request.form['id']
            if id and int(id) > 0:
                connection.remove_record(int(id))

            connection.close()

            return redirect(url_for('database_display'))

    def run(self):
        self.app.run(debug=True)
