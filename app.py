from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql #type: ignore
from flask import session
import re

app = Flask(__name__)
app.secret_key = 'storekey'

db_config = {
    'host': '10.2.3.123',
    'user': 'jonathan',
    'password': 'jonathan2007',
    'database': 'clothes_store'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

    try:
        conn = pymysql.connect(**db_config)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Logged in successfully! Velkommen {user[1]}', 'success')
            return redirect(url_for('profile', username=user[1]))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
    except Exception as e:
        flash(f"Error logging in: {e}", 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/women')
def women():
    return render_template('women.html')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)