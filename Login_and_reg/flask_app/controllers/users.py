from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_account():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    
    if not login.validate_register(request.form):
        return redirect('/')

    id = User.save(data)
    session[user_id] = id

    return redirect('/dashbord')

@app.route('/login', methods=['POST'])
def login():
    if not user:
        flash("Invalid Email", "login")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect Pasword", "login")
        return redirect('/')
    session['user_id'] = user.id
    user = User.get_by_email(request.form)
    return redirect('dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'id' : session['user_id']
    }
    return render_template('dashboard.html', user = User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')