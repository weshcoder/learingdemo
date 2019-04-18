from flask import Flask, render_template, flash, redirect, request, url_for
from .models import db, Users
from .forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'bee3d7c48f45083e800d8a505c396a6b'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:marthairungu123#@localhost/Flask-Bucket-list'
POSTGRES = {
    'user': 'postgres',
    'pw': 'marthairungu123#',
    'db': 'Flask-Bucket-list',
    'host': 'localhost',
    'port': '5432',
}
db.init_app(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        email = form.Email.data
        password = form.Password.data

        user = Users.query.filter_by(email=email).first()

        if user and user.password == password:
            flash(f'Congratulations, you logged in!')
            return redirect(url_for('home'))

        flash(f'Email or password incorrect')
        return redirect(url_for('login'))

    return render_template("login.html", title='Login', form=form)
    

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.Username.data
        email = form.Email.data
        password = form.Password.data

        user = Users(username=username, email=email, password=password)
        user.save()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template("register.html", title='Register', form=form)


@app.route("/trial")
def trial():
    return render_template("trial.html")


@app.route('/logged')
def logged():
    return render_template('logged.html')
