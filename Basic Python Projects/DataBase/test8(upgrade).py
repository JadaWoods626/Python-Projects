import sqlite3

conn = sqlite3.connect('test8.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")

    conn.commit()
conn.close()

conn = sqlite3.connect('test8.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
    VALUES (?, ?, ?)", ('Rainie', 'Cloud', 'RainieCloud@outlook.com'))

    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
    VALUES (?, ?, ?)", ('Mori', 'Jinn', 'MoriJinn@outlook.com'))
    
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
    VALUES (?, ?, ?)", ('Player', 'Unknown', 'PlayerUnknown@outlook.com'))

    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
    VALUES (?, ?, ?)", ('Obsidn', 'Ryujin', 'ObsidnRyujin@outlook.com'))

    conn.commit()
conn.close()

conn = sqlite3.connect('test8.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email \
    FROM tbl_persons WHERE col_fname = 'Player'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)



 cur.execute("INSERT INTO tbl_assignment223 (col_png, col_txt, col_docx, col_jpg, col_mpg) VALUES (?, ?, ?, ?, ?)", \
        ('NULL', 'World.txt', 'NULL', 'NULL', 'NULL'))

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txt FROM tbl_assignment223 WHERE col_txt = 'World.txt'")
    varText = cur.fetchall()
    for item in varText:
        msg = "Text File: {}".format(item)
    print(msg)
