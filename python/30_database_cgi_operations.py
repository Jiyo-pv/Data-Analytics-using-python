#!C:/Users/jiyop/AppData/Local/Programs/Python/Python314/python.exe

import cgi
import mysql.connector

print("Content-Type: text/html\n")

# MySQL connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cur = con.cursor()

# Create database and table
cur.execute("CREATE DATABASE IF NOT EXISTS cgidb")
cur.execute("USE cgidb")
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

form = cgi.FieldStorage()

act = form.getvalue("act", "")
sid = form.getvalue("id", "")
name = form.getvalue("name", "")
age = form.getvalue("age", "")

# CREATE
if act == "add":
    cur.execute("INSERT INTO student(name, age) VALUES(%s, %s)", (name, age))
    con.commit()

# UPDATE
elif act == "update":
    cur.execute(
        "UPDATE student SET name=%s, age=%s WHERE id=%s",
        (name, age, sid)
    )
    con.commit()

# DELETE
elif act == "delete":
    cur.execute("DELETE FROM student WHERE id=%s", (sid,))
    con.commit()

# EDIT
edit = None
if act == "edit":
    cur.execute("SELECT * FROM student WHERE id=%s", (sid,))
    edit = cur.fetchone()

print("<html><body>")
print("<h2>Student CRUD using CGI + MySQL</h2>")

# Form
if edit:
    print(f"""
    <form method="post" action="/cgi-bin/30_database_cgi_operations.py">
        <input type="hidden" name="act" value="update">
        <input type="hidden" name="id" value="{edit[0]}">

        Name: <input type="text" name="name" value="{edit[1]}"><br><br>
        Age: <input type="text" name="age" value="{edit[2]}"><br><br>

        <input type="submit" value="Update">
    </form>
    <hr>
    """)
else:
    print("""
    <form method="post" action="/cgi-bin/30_database_cgi_operations.py">
        <input type="hidden" name="act" value="add">

        Name: <input type="text" name="name"><br><br>
        Age: <input type="text" name="age"><br><br>

        <input type="submit" value="Add">
    </form>
    <hr>
    """)

# READ
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

print("<table border='1' cellpadding='6'>")
print("<tr><th>ID</th><th>Name</th><th>Age</th><th>Action</th></tr>")

for r in rows:
    print(f"""
    <tr>
        <td>{r[0]}</td>
        <td>{r[1]}</td>
        <td>{r[2]}</td>
        <td>
            <a href="/cgi-bin/30_database_cgi_operations.py?act=edit&id={r[0]}">Edit</a> |
            <a href="/cgi-bin/30_database_cgi_operations.py?act=delete&id={r[0]}">Delete</a>
        </td>
    </tr>
    """)

print("</table>")
print("</body></html>")

cur.close()
con.close()