from flask import Flask
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

            # Creates a simple html for database records
            records_string = ""
            for record in records:
                records_string += f'<p>{record}</p>\n<br>\n'

            return records_string

    def run(self):
        self.app.run(debug=True)
