import sqlite3
from flask import render_template, flash, redirect
from app import app
from app.forms import *


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Poland!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user={}, remember_me={}'.format(form.username.data, form.remember_me.data))
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        string = "INSERT INTO ListOfStudents(username,password) VALUES ('{}', '{}')".format(form.username.data, form.password.data)
        cursor.execute(string)
        conn.commit()
        cursor.execute('SELECT * FROM ListOfStudents')
        print(cursor.fetchall())
        return redirect('/index')
    return render_template('login.html', title='log In', form=form)


@app.route('/signup')
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Login requested for user={}, remember_me={}'.format(form.username.data, form.remember_me.data))
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        string = "INSERT INTO ListOfStudents(username,password) VALUES ('{}', '{}')".format(form.name.data, form.password.data)
        cursor.execute(string)
        conn.commit()
        cursor.execute('SELECT * FROM ListOfStudents')
        print(cursor.fetchall())
        return redirect('/index')
    return render_template('sign up.html', title='sign In', form=form)
