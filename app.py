from flask import Flask, redirect, render_template, request, escape, session, url_for
import json, sqlite3, jinja2

app = Flask(__name__, template_folder="templates", static_url_path="")
app.secret_key = b'ESJC7H9^YeNGz&Xak&#7R_K&FDQceA@Z-swKUr3RVW$xSR+$Q4F9&Sen5kveP*k-'

users = []
con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute(("SELECT * FROM users;"))
for x, y in cur.fetchall():
	users.append({
		"username": x,
		"password": y
		})
con.close()
print(users)

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
    usrnme = request.form['username']
    psswd = request.form['password']
    print(usrnme, psswd)
    for x in users:
      if x['username'] == usrnme:
        if x['password'] == psswd:
        	session['username']=usrnme
        	return redirect(url_for("index"))
        else:
        	return "wrong password"
    return 'No such user'

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
   con = sqlite3.connect('users.db')
   cur = con.cursor()
   cur.execute(("INSERT INTO users VALUES (?, ?)"), (request.form["username"], request.form["password"]))
   con.commit()
   con.close()
   users.append({
        "username": request.form['username'],
       	"password": request.form['password']
   })
   print(users)
   return "<h1 style='text-align: center;'>Registered!</h1>"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User '+escape(username)
