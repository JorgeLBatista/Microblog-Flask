from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/index')
def index():
    
    user = {'username': 'Jorge', 'password': '12345678'}
    
    posts = [
        {
            'author': {'username': 'Jorge'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Miguel'},
            'body': 'Hermano de la puta de Susan!'
        }
    ]    
    return render_template('index.html', title = 'Home', posts = posts, user = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login request user for {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', form = form)