from flask import Flask, render_template, redirect, flash, session, request
import jinja2
from cat import all_cats

app = Flask(__name__)

app.secret_key = 'mini-app-key'

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/cats')
def display_cats():

    return render_template('cats.html', cats_list=all_cats)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
