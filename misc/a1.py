import sqlite3
reg_users=0
conn = sqlite3.connect('../users.db')
cur = conn.cursor()
cur.execute(("SELECT * FROM users"))
for x in cur.fetchall():
	reg_users+=1
conn.close()
print(str(reg_users) + " registered users")
