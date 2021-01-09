from Blog.models import User, Post
from flask import render_template, url_for, flash, redirect
from Blog.forms import RegistrationForm, LoginForm
from Blog import app

posts = [
    {
        'author':'Enes Uguroglu',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20,2018'
    },
    {
        'author':'Dilara Uguroglu',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 21,2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed, Please check username and password', 'danger')
    return render_template('login.html', form=form)
