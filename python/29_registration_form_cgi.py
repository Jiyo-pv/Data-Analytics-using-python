#!C:\Users\jiyop\AppData\Local\Programs\Python\Python314\python.exe
# Q29 MSc Admission Registration Form using CGI - @JIYO P V 2026-09-06

import cgi
import html

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

if "name" in form:
    name = html.escape(form.getvalue("name", ""))
    email = html.escape(form.getvalue("email", ""))
    phone = html.escape(form.getvalue("phone", ""))
    course = html.escape(form.getvalue("course", ""))
    
    print("""
    <html>
    <body>
    <h1>Registration Successful</h1>
    <p>Thank you for registering!</p>
    <h3>Your Information:</h3>
    <table border="1">
    <tr><td>Name:</td><td>""" + name + """</td></tr>
    <tr><td>Email:</td><td>""" + email + """</td></tr>
    <tr><td>Phone:</td><td>""" + phone + """</td></tr>
    <tr><td>Course:</td><td>""" + course + """</td></tr>
    </table>
    <br>
    <a href="q29_registration.cgi">Register Another Student</a>
    </body>
    </html>
    """)
else:
    print("""
    <html>
    <body>
    <h1>MSc Admission Registration</h1>
    <form method="POST">
    <label>Name:</label><br>
    <input type="text" name="name" required><br><br>
    
    <label>Email:</label><br>
    <input type="email" name="email" required><br><br>
    
    <label>Phone:</label><br>
    <input type="tel" name="phone" required><br><br>
    
    <label>Course:</label><br>
    <select name="course" required>
    <option value="">Select Course</option>
    <option value="Data Science">Data Science</option>
    <option value="AI">Artificial Intelligence</option>
    <option value="Computer Science">Computer Science</option>
    </select><br><br>
    
    <button type="submit">Register</button>
    </form>
    </body>
    </html>
    """)
