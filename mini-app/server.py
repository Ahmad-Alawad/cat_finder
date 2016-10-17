from flask import Flask, render_template, redirect, flash, session, request
import jinja2
from cat import all_cats

app = Flask(__name__)

app.secret_key = 'mini-app-key'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/cats")
def list_cats():
    """Return page showing all cats"""
    if "user" in session:
        return render_template("all_cats.html",
                           cats_list=all_cats)
    else:
        flash("Please login first")
        return redirect("/login")

@app.route("/cat/<cat_name>")
def display_cat(cat_name):
    """Return page showing the details of a given cat."""
    for cat in all_cats:
        if cat.name == cat_name:
            display_cat = cat
            break

    return render_template("cat_details.html",
                           display_cat=display_cat)


@app.route("/login")
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login_process", methods=["POST"])
def process_login():

    email = request.form.get('email')
    password = request.form.get('password')
    if ((str(email) == "ahmad@hackbrightacademy.com") & (str(password) == '123')):
        session['user'] = 'ahmad'
        return redirect("/cats")
    else:
        flash("Login was unsucessful, try again.")
        return redirect("/login")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
