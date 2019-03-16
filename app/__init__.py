from flask  import Flask, render_template
from .models import db
from forms import RegestrationForm, LoginForm 


app = Flask(__name__)

app.config['SECRET_KEY'] =  'bee3d7c48f45083e800d8a505c396a6b'
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'
POSTGRES = {
    'user': 'postgres',
    'pw': 'marthairungu123#',
    'db': 'Flask-Bucket-list',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/login")
def login():
  form = LoginForm()
  return render_template("login.html", title='Login', form = form) 

@app.route("/register")
def register():
  form = RegestrationForm()
  return render_template("register.html", title='Register', form = form)

@app.route("/trial")
def trial():
  return render_template("trial.html")
    