import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_eemail TEXT \
        )")

    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_eemail) \
    VALUES (?, ?, ?)", ('Rainie', 'Cloud', 'RainieCloud@outlook.com'))

    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_eemail) \
    VALUES (?, ?, ?)", ('Mori', 'Jinn', 'MoriJinn@outlook.com'))
    
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_eemail) \
    VALUES (?, ?, ?)", ('Player', 'Unknown', 'PlayerUnknown@outlook.com'))

    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_eemail) \
    VALUES (?, ?, ?)", ('Obsidn', 'Ryujin', 'ObsidnRyujin@outlook.com'))

    conn.commit()
conn.close()


