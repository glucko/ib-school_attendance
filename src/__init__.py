from flask import Flask, redirect, url_for, flash, render_template, request
from .models import db
from .cli import create_db, print_db, add_student


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdfwerqewgfgzvzxc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.cli.add_command(print_db)
app.cli.add_command(create_db)
app.cli.add_command(add_student)
db.init_app(app)

if __name__ == "__main__":
        app.run(debug=True)