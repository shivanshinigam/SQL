import sqlite3
import re
from datetime import datetime
import csv

DB_PATH = "./interns.db"

def print_header(title):
    print("\n======", title, "======")

# =============================
# BASIC PYTHON TASKS
# =============================

def task_1():
    print_header("Q1 List Indexing")
    lst = ["Asha", "Rohan", "Simran"]
    print(lst[1])

def task_2():
    print_header("Q2 Append to List")
    lst = ["Asha", "Rohan"]
    lst.append("Simran")
    print(lst)

def task_3():
    print_header("Q3 Enumerate List")
    for i, x in enumerate(["A", "B", "C"], start=1):
        print(i, x)

def task_4():
    print_header("Q4 Tuple Access")
    t = (101, "Asha", "Patel")
    print(t[1])

def task_5():
    print_header("Q5 Tuple Immutability")
    t = (1, 2, 3)
    try:
        t[1] = 99
    except Exception as e:
        print("Error:", e)

def task_6():
    print_header("Q6 Set Uniqueness")
    s = {"Mumbai", "Pune", "Pune"}
    print(s)

def task_7():
    print_header("Q7 Add/Remove Set")
    s = {"A", "B"}
    s.add("C")
    s.discard("A")
    print(s)

def task_8():
    print_header("Q8 Dict Access")
    d = {"id":101, "name":"Asha", "email":"a@x.com"}
    print(d["email"])

def task_9():
    print_header("Q9 Update Dict")
    d = {"id":101, "name":"Asha"}
    d["name"] = "Asha Patel"
    print(d)

def task_10():
    print_header("Q10 Loop Dict")
    d = {"a":1,"b":2}
    for k,v in d.items():
        print(k, v)

def task_11():
    print_header("Q11 Sum List")
    lst=[1,2,3]
    print(sum(lst))

def task_12():
    print_header("Q12 While Loop")
    i=1
    while i<=3:
        print(i)
        i+=1

def task_13():
    print_header("Q13 Average")
    lst=[10,20,30]
    print(sum(lst)/len(lst))

def task_14():
    print_header("Q14 Iterator Next")
    it=iter(["A","B","C"])
    print(next(it)); print(next(it)); print(next(it))

def task_15():
    print_header("Q15 List Comprehension")
    print([x.upper() for x in ["a","b"]])

def task_16():
    print_header("Q16 Filter > 2")
    print([x for x in [1,2,3,4] if x>2])

def task_17():
    print_header("Q17 Map + Filter")
    print(list(map(lambda x:x*2, [1,2,3])))
    print(list(filter(lambda x:x%2==0, [1,2,3,4])))

def task_18():
    print_header("Q18 Parse Date")
    d=datetime.strptime("2025-12-01","%Y-%m-%d")
    print(d.year, d.strftime("%d %b %Y"))

def task_19():
    print_header("Q19 Days Between")
    a=datetime(2025,12,1)
    b=datetime(2025,11,10)
    print((a-b).days)

def task_20():
    print_header("Q20 Regex Starts With S")
    names=["Simran","Asha","Sahil"]
    print([n for n in names if re.match(r"^S", n)])

# =============================
# ADVANCED PYTHON
# =============================

def task_21():
    print_header("Q21 Regex Replace Domain")
    email="asha@example.com"
    print(re.sub(r"@.*","@uni.edu", email))

def task_22():
    print_header("Q22 Simple CSV Parse")
    text="101,Asha\n102,Rohan"
    rows=[line.split(",") for line in text.splitlines()]
    print(rows)

# =============================
# SQLITE TASKS
# =============================

def sql_show(conn, query):
    cur=conn.cursor()
    cur.execute(query)
    rows=cur.fetchall()
    for r in rows: print(r)
    return rows

def task_23(conn):
    print_header("Q23 SELECT internprofile")
    sql_show(conn,"SELECT * FROM internprofile;")

def task_24(conn):
    print_header("Q24 INSERT new intern id=200")
    conn.execute("INSERT OR IGNORE INTO internprofile VALUES (200,'Test','User','t@x.com','Uni',2026,'City')")
    conn.commit()
    sql_show(conn,"SELECT * FROM internprofile WHERE intern_id=200;")

def task_25(conn):
    print_header("Q25 WHERE + ORDER")
    sql_show(conn,"SELECT first_name, city FROM internprofile WHERE city='Pune' ORDER BY first_name;")

def task_26(conn):
    print_header("Q26 JOIN 3 Tables")
    sql_show(conn,"""
SELECT p.first_name, c.company_name, s.stipend
FROM internprofile p
JOIN internsalary s ON p.intern_id=s.intern_id
JOIN codecompanyinterns c ON c.internship_id=s.internship_id;
""")

def task_27(conn):
    print_header("Q27 UPDATE stipend")
    conn.execute("UPDATE internsalary SET stipend=36000 WHERE salary_id=1002")
    conn.commit()
    sql_show(conn,"SELECT salary_id, stipend FROM internsalary WHERE salary_id=1002;")

def task_28(conn):
    print_header("Q28 DELETE row")
    conn.execute("DELETE FROM internsalary WHERE salary_id=1003")
    conn.commit()
    sql_show(conn,"SELECT * FROM internsalary;")

def task_29(conn):
    print_header("Q29 CREATE temp table")
    conn.execute("CREATE TABLE IF NOT EXISTS temp_demo(id INT, note TEXT)")
    conn.commit()
    sql_show(conn,"SELECT * FROM temp_demo;")

def task_30(conn):
    print_header("Q30 DROP temp table")
    conn.execute("DROP TABLE IF EXISTS temp_demo")
    conn.commit()
    print("Dropped temp_demo")

def task_31(conn):
    print_header("Q31 Transaction Rollback")
    try:
        conn.execute("BEGIN")
        conn.execute("INSERT INTO internprofile VALUES (300,'Tx','One','t1@x.com','U',2025,'C')")
        conn.rollback()
    except:
        conn.rollback()
    sql_show(conn,"SELECT * FROM internprofile WHERE intern_id=300;")

def task_32(conn):
    print_header("Q32 fetchone vs fetchall")
    cur=conn.cursor()
    cur.execute("SELECT intern_id FROM internprofile")
    print("one:",cur.fetchone())
    print("rest:",cur.fetchall())

def task_33(conn):
    print_header("Q33 executemany")
    data=[(401,'A','B','a@x.com','U',2026,'C'),
          (402,'D','E','d@x.com','U',2026,'C')]
    conn.executemany("INSERT OR IGNORE INTO internprofile VALUES (?,?,?,?,?,?,?)",data)
    conn.commit()
    sql_show(conn,"SELECT intern_id FROM internprofile WHERE intern_id IN(401,402);")

def task_34(conn):
    print_header("Q34 row_factory dict")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute("SELECT * FROM internprofile LIMIT 1")
    row=cur.fetchone()
    print(dict(row))
    conn.row_factory=None

def task_35(conn):
    print_header("Q35 LIKE via SQL")
    sql_show(conn,"SELECT first_name FROM internprofile WHERE first_name LIKE '%a%';")

def task_36(conn):
    print_header("Q36 Insert Timestamp")
    now=datetime.now().isoformat()
    conn.execute("CREATE TABLE IF NOT EXISTS logs(id INTEGER,ts TEXT,msg TEXT)")
    conn.execute("INSERT INTO logs VALUES (1,?,?)",(now,"Log entry"))
    conn.commit()
    sql_show(conn,"SELECT * FROM logs;")

def task_37(conn):
    print_header("Q37 Regex Validate Email")
    email="new@x.com"
    if re.match(r"^[\\w.-]+@[\\w.-]+\\.\\w+$", email):
        conn.execute("INSERT OR IGNORE INTO internprofile VALUES (500,'Reg','User',?,?,?,?)",
                     (email,"Uni",2026,"City"))
        conn.commit()
        print("Inserted")
    else:
        print("Invalid")

def task_38(conn):
    print_header("Q38 Generator Insert")
    def gen(start=600):
        n=start
        while True:
            yield n; n+=1
    g=gen()
    for _ in range(2):
        iid=next(g)
        conn.execute("INSERT OR IGNORE INTO internprofile VALUES (?,?,?,?,?,?,?)",
                     (iid,f"G{iid}","User",f"g{iid}@x.com","Uni",2026,"City"))
    conn.commit()
    sql_show(conn,"SELECT intern_id FROM internprofile WHERE intern_id>=600 LIMIT 5;")

def task_39(conn):
    print_header("Q39 Iterate Cursor")
    cur=conn.cursor()
    cur.execute("SELECT intern_id,first_name FROM internprofile LIMIT 5")
    for r in cur: print(r)

def task_40(conn):
    print_header("Q40 Export CSV")
    cur=conn.cursor()
    cur.execute("SELECT intern_id,first_name,last_name,email FROM internprofile")
    rows=cur.fetchall()
    with open("interns_export.csv","w",newline="") as f:
        csv.writer(f).writerows(rows)
    print("Exported CSV")

def main():
    # Run Python-only tasks
    for t in [task_1,task_2,task_3,task_4,task_5,task_6,task_7,task_8,task_9,task_10,
              task_11,task_12,task_13,task_14,task_15,task_16,task_17,task_18,task_19,task_20,
              task_21,task_22]:
        t()

    # DB tasks
    conn=sqlite3.connect(DB_PATH)
    for t in [task_23,task_24,task_25,task_26,task_27,task_28,task_29,task_30,
              task_31,task_32,task_33,task_34,task_35,task_36,task_37,task_38,task_39,task_40]:
        t(conn)
    conn.close()

if __name__ == "__main__":
    main()
