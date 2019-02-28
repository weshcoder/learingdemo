from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    