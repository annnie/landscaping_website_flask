from markupsafe import escape
import sqlite3
from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit/')
def submit():
    return render_template('gallery.html')

# @app.route('/contact/')
# def contact():
#     return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
