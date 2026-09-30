import sqlite3
def create_db():
    con = sqlite3.connect("emp.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS e_salary (
    emp_code TEXT PRIMARY KEY,
    designation TEXT,
    name TEXT,
    age TEXT,
    gender TEXT,
    email TEXT,
    hr_location TEXT,
    dob TEXT,
    doj TEXT,
    proof_id TEXT,
    contact TEXT,
    status TEXT,
    experience TEXT,
    address TEXT,
    month TEXT,
    year TEXT,
    basic_salary TEXT,
    total_days TEXT,
    absent TEXT,
    medical TEXT,
    pf TEXT,
    convence TEXT,
    net_salary TEXT,
    salary_reciept TEXT)""")

    con.commit()
    con.close()
    print("Database and table created successfully.")
create_db()
