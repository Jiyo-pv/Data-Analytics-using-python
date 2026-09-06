#!C:\Users\jiyop\AppData\Local\Programs\Python\Python314\python.exe
# Q30 Database CGI Operations (CRUD) - @JIYO P V 2026-09-06

import cgi
import sqlite3
import html

DB_FILE = "products.db"

def init_database():
    """Initialize database and create table if not exists"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_product(name, price, quantity):
    """INSERT operation"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", 
                   (name, float(price), int(quantity)))
    conn.commit()
    conn.close()

def select_all_products():
    """SELECT operation - retrieve all products"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def update_product(product_id, name, price, quantity):
    """UPDATE operation"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=?, price=?, quantity=? WHERE id=?",
                   (name, float(price), int(quantity), product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    """DELETE operation"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

print("Content-Type: text/html\n")

init_database()
form = cgi.FieldStorage()

# Handle INSERT operation
if "action" in form and form.getvalue("action") == "insert" and "name" in form:
    name = html.escape(form.getvalue("name", ""))
    price = form.getvalue("price", "0")
    quantity = form.getvalue("quantity", "0")
    insert_product(name, float(price), int(quantity))

# Handle UPDATE operation
if "action" in form and form.getvalue("action") == "update" and "id" in form and "name" in form:
    pid = form.getvalue("id", "")
    name = html.escape(form.getvalue("name", ""))
    price = form.getvalue("price", "0")
    quantity = form.getvalue("quantity", "0")
    update_product(pid, name, float(price), int(quantity))

# Handle DELETE operation
if "action" in form and form.getvalue("action") == "delete" and "id" in form:
    pid = form.getvalue("id", "")
    delete_product(pid)

# Display all products
products = select_all_products()
product_rows = ""
if products:
    for p in products:
        product_rows += f"<tr><td>{p[0]}</td><td>{p[1]}</td><td>${p[2]:.2f}</td><td>{p[3]}</td><td><a href='?action=delete&id={p[0]}'>Delete</a></td></tr>"
else:
    product_rows = "<tr><td colspan='5' style='text-align:center;'>No products</td></tr>"

print(f"""
<html>
<body style='font-family: Arial, sans-serif; margin: 20px;'>
<h1>Product Database Management</h1>

<h2>Add Product</h2>
<form method="POST">
<input type="hidden" name="action" value="insert">
Name: <input type="text" name="name" required><br>
Price: <input type="number" name="price" step="0.01" required><br>
Quantity: <input type="number" name="quantity" required><br>
<button type="submit">Add Product</button>
</form>

<h2>All Products</h2>
<table border="1" cellpadding="10">
<tr style='background-color: #4CAF50; color: white;'><th>ID</th><th>Name</th><th>Price</th><th>Quantity</th><th>Action</th></tr>
{product_rows}
</table>
</body>
</html>
""")
