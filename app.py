from flask import Flask, redirect, render_template, request, session, url_for
from markupsafe import escape
import json, sqlite3 as sql, jinja2
import secrets, string

app = Flask(__name__, template_folder="templates", static_url_path="")
app.secret_key = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(64))

users = []
def depr():
    con = sql.connect('users.db')
    cur = con.cursor()
    cur.execute(("SELECT * FROM users;"))
    data = cur.fetchall()
    con.close()
    print(data)



@app.route('/')
def index():
	if 'username' in session:
		return render_template('index.html', username=session['username'])
	else:
		return render_template('index.html', username="")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    data = []
    usrnme = request.form['username']
    psswd = request.form['password']
    with sql.connect("users.db") as conn:
        data = conn.execute("SELECT * FROM users;")
        data = data.fetchall()
    for x, y in data:
        print("Form username: "+usrnme, psswd)
        if x == usrnme:
            if y == psswd:
                session['username']=usrnme
                return redirect(url_for("index"))
            else:
                return "wrong password"
        else:
            return 'No such user'
    return "", 500

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
   with sql.connect('users.db') as conn:
        conn.cursor().execute(("INSERT INTO users VALUES (?, ?)"), (request.form["username"], request.form["password"]))
        conn.commit()
   print(users)
   return "<h1 style='text-align: center;'>Registered!</h1>"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User '+escape(username)

app.run('0.0.0.0', debug=True)