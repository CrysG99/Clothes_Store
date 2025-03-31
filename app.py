from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql #type: ignore
from flask import session
import re

app = Flask(__name__)
app.secret_key = 'storekey'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/women')
def women():
    return render_template('women.html')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)