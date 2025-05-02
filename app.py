from flask import Flask


class App():
    # When app is initialised
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/")
        def home():
            return "<p>Hello, World!</p>"

    def run(self):
        self.app.run(debug=True)
