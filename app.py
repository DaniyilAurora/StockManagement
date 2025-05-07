from flask import Flask, render_template, request, redirect, url_for, session
from database import Database
from connection import Connection
import hashlib


class App():
    # When app is initialised
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'some_secret_key'
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

        @self.app.route("/login")
        def login():
            return render_template("login.html")

        @self.app.route("/loginAttempt", methods=['POST'])
        def login_attempt():
            username = request.form['username'].strip()
            password = request.form['password'].strip()

            encoded_password = hashlib.md5(password.encode()).hexdigest()

            connection = Connection()
            id = connection.get_id(username, encoded_password)
            if id:
                session['user_id'] = id
                return redirect('/db')
            else:
                return 'Invalid credentials!'

        @self.app.route("/db")
        def database_display():
            # If user is not logged in, send to /login page
            if 'user_id' not in session:
                return redirect('/login')
            
            connection = Connection()
            records = connection.get_records()
            categories = connection.get_categories()
            connection.close()

            return render_template("index.html", records=records, categories=categories)

        @self.app.route("/addStock", methods=['POST'])
        def add_stock():
            connection = Connection()

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

            id = request.form['id']
            if id and int(id) > 0:
                connection.remove_record(int(id))

            connection.close()

            return redirect(url_for('database_display'))

    def run(self):
        self.app.run(debug=True)
