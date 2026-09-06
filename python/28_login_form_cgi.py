#!C:\Users\jiyop\AppData\Local\Programs\Python\Python314\python.exe
# Q28 Login Form using CGI - @JIYO P V 2026-09-06

import cgi
import html

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

if "username" in form and "password" in form:
    username = html.escape(form.getvalue("username", ""))
    password = form.getvalue("password", "")
    
    print("""
    <html>
    <body>
    <h1>Login Result</h1>
    <p>Welcome """ + username + """!</p>
    <p>Username: """ + username + """</p>
    <p>Password: """ + ("*" * len(password)) + """</p>
    <a href="q28_login.cgi">Back to Login</a>
    </body>
    </html>
    """)
else:
    print("""
    <html>
    <body>
    <h1>Login Form</h1>
    <form method="POST">
    <label>Username:</label><br>
    <input type="text" name="username" required><br><br>
    <label>Password:</label><br>
    <input type="password" name="password" required><br><br>
    <button type="submit">Login</button>
    </form>
    </body>
    </html>
    """)
