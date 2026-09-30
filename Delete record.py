import sqlite3
con = sqlite3.connect("emp.db")
cur = con.cursor()
cur.execute("PRAGMA table_info(e_salary)")
print(cur.fetchall())
con.close()

