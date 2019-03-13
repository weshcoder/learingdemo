from flask  import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)
app.config['DEBUG'] = True

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'
POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/signup")
def signup():
  return render_template("signup.html")

@app.route("/trial")
def trial():
  return render_template("trial.html")
    