from flask import Flask, render_template
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
        def debugDatabase():
            connection = Connection()
            records = connection.get_records()
            connection.close()

            return render_template("index.html", records=records)

    def run(self):
        self.app.run(debug=False)
