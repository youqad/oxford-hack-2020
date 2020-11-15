from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mA7OumwKVZQr9ousrge1OVQxQr51WEs7'

@app.route('/')
def index():
    return render_template('index.html')