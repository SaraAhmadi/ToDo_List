import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask import Blueprint, render_template

app = Flask(__name__, template_folder='templates')  # still relative to module

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return render_template('login.html')

