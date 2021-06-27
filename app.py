<<<<<<< HEAD
from flask import Flask, redirect, render_template, request, escape, session, url_for
=======
from flask import Flask, render_template, request, escape, session, url_for
>>>>>>> 27a17ced7e6239aa0af54c5158c2f3147d5c1f53
import json, sqlite3

app = Flask(__name__, template_folder="templates", static_url_path="")
app.secret_key = b'ESJC7H9^YeNGz&Xak&#7R_K&FDQceA@Z-swKUr3RVW$xSR+$Q4F9&Sen5kveP*k-'

users = []
<<<<<<< HEAD
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
=======
>>>>>>> 27a17ced7e6239aa0af54c5158c2f3147d5c1f53

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    usrnme = request.form['username']
    psswd = request.form['password']
<<<<<<< HEAD
    print(usrnme, psswd)
    for x in users:
      if x['username'] == usrnme:
        if x['password'] == psswd:
        	session['username']=usrnme
        	return redirect(url_for(".show_user_profile", session['username']))
        else:
        	return "wrong password"
    return 'No such user'
=======
    for x in users:
        if x['username'] == usrnme:
            if x['password'] == psswd:
                session['username']=usrnme
                return "logged in"
                return redirect(url_for(f"show_user_profile{session['username']}"))
            else:
                return "wrong password"
        else:
            return "Wrong username"
    return 'text'
            
    
>>>>>>> 27a17ced7e6239aa0af54c5158c2f3147d5c1f53

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
<<<<<<< HEAD
   return "<h1 style='text-align: center;'>Registered!</h1>"
=======
   return "registered"
>>>>>>> 27a17ced7e6239aa0af54c5158c2f3147d5c1f53

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'
