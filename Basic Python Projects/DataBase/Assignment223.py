import sqlite3

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment223 ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_png TEXT, \
        col_txt TEXT, \
        col_docx TEXT, \
        col_mpg TEXT, \
        col_jpg TEXT \
        )")

    conn.commit()
conn.close()

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_assignment223 (col_png, col_txt, col_docx, col_jpg, col_mpg) VALUES (?, ?, ?, ?, ?)", \
        ('myImage.png', 'Hello.txt', 'information.docx', 'myPhoto.jpg', 'myMovie.mpg'))

    cur.execute("INSERT INTO tbl_assignment223 (col_png, col_txt, col_docx, col_jpg, col_mpg) VALUES (?, ?, ?, ?, ?)", \
        ('NULL', 'World.txt', 'NULL', 'NULL', 'NULL'))

    conn.commit()
conn.close()

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txt FROM tbl_assignment223 WHERE col_txt = 'Hello.txt'")
    varText = cur.fetchall()
    for item in varText:
        msg = "Text File: {}".format(item)
    print(msg)

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txt FROM tbl_assignment223 WHERE col_txt = 'World.txt'")
    varText = cur.fetchall()
    for item in varText:
        msg = "Text File: {}".format(item)
    print(msg)
