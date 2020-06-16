from flask import Flask, request, g, render_template, session, redirect, url_for
from main_db import MainData

app = Flask(__name__)
app.secret_key = 'very secret string'

data = None

@app.teardown_appcontext
def close_connection(exception):
    data.close_connection()

"""
Denne funktion sørger for at pakke den template, der skal vises,
ind i nogle standard-ting, f.eks. loginstatus.

my_render bør kaldes i stedet for at kalde render_template direkte.
"""
def my_render(template, **kwargs):
    login_status = get_login_status()
    if login_status:
        return render_template(template, loggedin=login_status, user = session['currentuser'], **kwargs)
    else:
        return render_template(template, loggedin=login_status, user = '', **kwargs)

@app.route("/")
@app.route("/home")
def home():
    return my_render('index.html')

@app.route("/register_user")
def register_user():
    return my_render('register_user.html', success = True, complete = True, title = 'Register user')
    

if __name__ == "__main__":
    with app.app_context():
        data = MainData()