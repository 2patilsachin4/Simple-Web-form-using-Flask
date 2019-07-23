from flask import render_template
from web import app
from web.forms import LoginForm

@app.route('/login')

def login():
    form = LoginForm()
    return render_template('login.html',title='Sign In', form = form)   
