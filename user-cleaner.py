import sqlite3
con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute(("DELETE FROM users"))
con.commit()
con.close()

