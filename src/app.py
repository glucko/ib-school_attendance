from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .cli import print_db, create_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdfwerqewgfgzvzxc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
app.cli.add_command(print_db)
app.cli.add_command(create_db)

@app.route('/api/getqr/<int:id>', methods=['GET'])
def get_qr(id):
    pass

@app.route('/api/signin/<int:id>', methods=['POST'])
def signin(id):
    pass
