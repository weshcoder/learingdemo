from flask  import Flask, render_template, flash, redirect, request
from .models import db, Users
from .forms import RegistrationForm, LoginForm 


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

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()

  if request.method == 'POST':
    print("\n\n" + str(request.data.decode()) + "\n\n")

    username = str(request.data.get('username', ''))
    email = str(request.data.get('email', ''))
    password = str(request.data.get('password', ''))

    if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!', 'success')

      user = Users(username=username, email=email, password=password)
      user.save()

  return render_template("register.html", title='Register', form = form)
@app.route("/trial")
def trial():
  return render_template("trial.html")

@app.route('/logged')
def logged():
  return render_template('logged.html')
    