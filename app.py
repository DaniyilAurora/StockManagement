from flask import Flask
from database import Database


class App():
    # When app is initialised
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_database()
        self.setup_routes()

    # Setup database for the app
    def setup_database(self):
        database = Database()

    # Setup routes for the app
    def setup_routes(self):
        @self.app.route("/")
        def home():
            return "<p>Hello, World!</p>"

    def run(self):
        self.app.run(debug=True)
