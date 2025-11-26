

import sqlite3
import re
import csv
from datetime import datetime

DB_PATH = "./interns.db"

def print_header(title):
    print("\n" + "="*6 + " " + title + " " + "="*6)

def sql_select(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    cols = [d[0] for d in cur.description] if cur.description else []
    rows = cur.fetchall()
    if cols:
        print(" | ".join(cols))
        for r in rows:
            print(" | ".join(str(x) if x is not None else 'NULL' for x in r))
    else:
        print("(no columns returned)")
    return rows

def safe_exec(conn, query, params=()):
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("SQL Error:", e)

# ---------------- PYTHON-ONLY TASKS ----------------

def task_1():
    print_header("Q1 list index")
    names = ["Asha","Rohan","Simran","Vikram"]
    print(names[2])

def task_2():
    print_header("Q2 append")
    x = ["A","B"]
    x.append("C")
    print(x)

def task_3():
    print_header("Q3 enumerate")
    for i,n in enumerate(["A","B","C"],1):
        print(i,n)

def task_4():
    print_header("Q4 tuple access")
    t = (101,"Asha","Patel")
    print(t[1])

def task_5():
    print_header("Q5 tuple immutability")
    t = (101,"Asha","Patel")
    try:
        t[1] = "X"
    except Exception as e:
        print("Error:", e)

def task_6():
    print_header("Q6 set unique")
    s = {"Mumbai","Pune","Mumbai"}
    print(s)

def task_7():
    print_header("Q7 set add/remove")
    s = {"A","B"}
    s.add("C")
    s.discard("B")
    print(s)

def task_8():
    print_header("Q8 dict access")
    d = {"id":101,"email":"a@x.com"}
    print(d["email"])

def task_9():
    print_header("Q9 dict update")
    d = {"email":"a@x.com"}
    d["email"] = "b@x.com"
    print(d)

def task_10():
    print_header("Q10 dict loop")
    d = {"id":101,"name":"Asha"}
    for k,v in d.items():
        print(k,v)

def task_11():
    print_header("Q11 sum loop")
    arr = [1,2,3]
    s = 0
    for x in arr:
        s += x
    print(s)

def task_12():
    print_header("Q12 while")
    i=1
    while i<=3:
        print(i)
        i+=1

def task_13():
    print_header("Q13 average list")
    x = [40,38,30]
    print(sum(x)/len(x))

def task_14():
    print_header("Q14 iterator")
    it = iter(["Asha","Rohan","Simran"])
    print(next(it))
    print(next(it))
    print(next(it))

def task_15():
    print_header("Q15 list comprehension")
    print([n.upper() for n in ["a","b","c"]])

def task_16():
    print_header("Q16 filter > 2")
    print([x for x in [1,2,3,4] if x>2])

def task_17():
    print_header("Q17 map/filter")
    print(list(map(lambda x:x*2,[1,2,3])))
    print(list(filter(lambda x:x%2==0,[1,2,3,4])))

def task_18():
    print_header("Q18 date parse/format")
    d = datetime.strptime("2025-12-01","%Y-%m-%d")
    print(d.strftime("%d %b %Y"))

def task_19():
    print_header("Q19 date diff")
    a = datetime(2025,12,1)
    b = datetime(2025,11,10)
    print((a-b).days)

def task_20():
    print_header("Q20 regex startswith S")
    names = ["Simran","Asha","Sahil"]
    print([n for n in names if re.match(r'^s',n,re.I)])

def task_21():
    print_header("Q21 regex replace domain")
    print(re.sub(r"@.*$", "@college.edu", "asha@example.com"))

def task_22():
    print_header("Q22 CSV parse")
    text="101,Asha\n102,Rohan"
    rows=[line.split(",") for line in text.splitlines()]
    print(rows)

# ---------------- SQLITE TASKS ----------------

def task_23(conn):
    print_header("Q23 SELECT *")
    sql_select(conn,"SELECT * FROM internprofile;")

def task_24(conn):
    print_header("Q24 insert new intern id=200")
    safe_exec(conn,"INSERT OR IGNORE INTO internprofile VALUES (200,'Test','User','t@x.com','TU',2026,'City')")
    sql_select(conn,"SELECT intern_id,first_name FROM internprofile WHERE intern_id=200;")

def task_25(conn):
    print_header("Q25 WHERE + ORDER")
    sql_select(conn,"SELECT intern_id,first_name FROM internprofile WHERE city='Pune' ORDER BY first_name;")

def task_26(conn):
    print_header("Q26 JOIN 3 tables")
    sql_select(conn,"""
SELECT p.first_name||' '||p.last_name AS name,c.company_name,s.stipend
FROM internprofile p
JOIN internsalary s ON p.intern_id=s.intern_id
JOIN codecompanyinterns c ON s.internship_id=c.internship_id;
""")

def task_27(conn):
    print_header("Q27 UPDATE")
    safe_exec(conn,"UPDATE internsalary SET stipend=36000 WHERE salary_id=1002")
    sql_select(conn,"SELECT salary_id,stipend FROM internsalary WHERE salary_id=1002;")

def task_28(conn):
    print_header("Q28 DELETE")
    safe_exec(conn,"DELETE FROM internsalary WHERE salary_id=1003")
    sql_select(conn,"SELECT * FROM internsalary;")

def task_29(conn):
    print_header("Q29 CREATE temp table")
    safe_exec(conn,"CREATE TABLE IF NOT EXISTS temp_demo(id INTEGER PRIMARY KEY,note TEXT)")
    sql_select(conn,"SELECT * FROM temp_demo;")

def task_30(conn):
    print_header("Q30 DROP temp table")
    safe_exec(conn,"DROP TABLE IF EXISTS temp_demo")
    print("Dropped temp_demo")

def task_31(conn):
    print_header("Q31 transaction rollback")
    try:
        conn.execute("BEGIN")
        conn.execute("INSERT INTO internprofile VALUES (300,'Tx','One','x','U',2026,'C')")
        conn.execute("INSERT INTO internprofile VALUES (301,'Tx','Two','y','U',2026,'C')")
        conn.rollback()
    except:
        conn.rollback()
    sql_select(conn,"SELECT intern_id FROM internprofile WHERE intern_id IN (300,301);")

def task_32(conn):
    print_header("Q32 fetchone/fetchall")
    cur=conn.cursor()
    cur.execute("SELECT intern_id FROM internprofile")
    print("one:",cur.fetchone())
    print("rest:",len(cur.fetchall()))

def task_33(conn):
    print_header("Q33 executemany")
    data=[(401,'A','B','a','U',2026,'X'),(402,'C','D','c','U',2026,'Y')]
    conn.executemany("INSERT OR IGNORE INTO internprofile VALUES (?,?,?,?,?,?,?)",data)
    conn.commit()
    sql_select(conn,"SELECT intern_id,first_name FROM internprofile WHERE intern_id IN (401,402);")

def task_34(conn):
    print_header("Q34 row_factory dict")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute("SELECT * FROM internprofile LIMIT 1")
    print(dict(cur.fetchone()))
    conn.row_factory=None

def task_35(conn):
    print_header("Q35 LIKE")
    sql_select(conn,"SELECT first_name FROM internprofile WHERE first_name LIKE '%a%';")

def task_36(conn):
    print_header("Q36 insert timestamp")
    now=datetime.now().isoformat()
    safe_exec(conn,"CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY,ts TEXT,msg TEXT)")
    safe_exec(conn,"INSERT INTO logs(ts,msg) VALUES(?,?)",(now,"log"))
    sql_select(conn,"SELECT * FROM logs ORDER BY id DESC LIMIT 1;")

def task_37(conn):
    print_header("Q37 regex validate email")
    email="new@example.com"
    if re.match(r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$',email):
        safe_exec(conn,"INSERT OR IGNORE INTO internprofile VALUES (500,'Reg','User',?, 'U',2026,'C')",(email,))
    sql_select(conn,"SELECT intern_id,email FROM internprofile WHERE intern_id=500;")

def task_38(conn):
    print_header("Q38 generator ids")
    def gen(n=600):
        while True:
            yield n
            n+=1
    g=gen()
    i1=next(g); i2=next(g)
    safe_exec(conn,"INSERT OR IGNORE INTO internprofile VALUES (?, 'G','One','g@x','U',2026,'C')",(i1,))
    safe_exec(conn,"INSERT OR IGNORE INTO internprofile VALUES (?, 'G','Two','h@x','U',2026,'C')",(i2,))
    sql_select(conn,"SELECT intern_id FROM internprofile WHERE intern_id>=600 LIMIT 5;")

def task_39(conn):
    print_header("Q39 cursor iterate")
    cur=conn.cursor()
    cur.execute("SELECT intern_id,first_name FROM internprofile LIMIT 5")
    for r in cur:
        print(r)

def task_40(conn):
    print_header("Q40 export CSV")
    cur=conn.cursor()
    cur.execute("SELECT intern_id,first_name,last_name,email FROM internprofile")
    rows=cur.fetchall()
    with open("interns_export.csv","w",newline="") as f:
        w=csv.writer(f)
        w.writerow([d[0] for d in cur.description])
        w.writerows(rows)
    print("Exported CSV")

def main():
    # python tasks
    for i in range(1,23):
        globals()[f"task_{i}"]()

    # db tasks
    conn=sqlite3.connect(DB_PATH)
    try:
        for i in range(23,41):
            globals()[f"task_{i}"](conn)
    finally:
        conn.close()

    print_header("DONE all tasks")

if __name__=="__main__":
    main()
PY
