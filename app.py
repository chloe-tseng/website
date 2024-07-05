# March 27, 2024 - April 3, 2024

# python3 -m flask --app app run --debug
from flask import Flask, render_template, request

import time

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')
 
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

# how to open a website:
# 1. go to folder and "web.app"
# 2. open a terminal in that file, hold down and find the button
# 3. type python3 -m flask run
# 4. type python3 -m flask run --debug