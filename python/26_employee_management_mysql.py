# Q26 Employee Management System using MySQL - @JIYO P V 2026-09-06
# Note: Requires mysql-connector-python. Install: pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

# MySQL connection configuration
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Change to your MySQL password
    'database': 'employee_db'
}

def connect_db():
    """Establish connection with MySQL database"""
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Connection error: {e}")
        return None

def create_database(conn):
    """Create database if not exists"""
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
        cursor.execute("USE employee_db")
        conn.commit()
        print("Database created/selected successfully")
    except Error as e:
        print(f"Error creating database: {e}")

def create_table(conn):
    """Create Employee table with constraints"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employee (
                Emp_ID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(100) NOT NULL,
                Department VARCHAR(100) NOT NULL,
                Salary DECIMAL(10,2) NOT NULL,
                Designation VARCHAR(100) NOT NULL
            )
        """)
        conn.commit()
        print("Employee table created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_employee(conn, name, department, salary, designation):
    """Insert a new employee using parameterized queries"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Employee (Name, Department, Salary, Designation)
            VALUES (%s, %s, %s, %s)
        """, (name, department, salary, designation))
        conn.commit()
        print(f"Employee '{name}' inserted successfully. ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error inserting employee: {e}")

def insert_multiple_employees(conn, employees):
    """Insert multiple employee records using executemany()"""
    try:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO Employee (Name, Department, Salary, Designation)
            VALUES (%s, %s, %s, %s)
        """, employees)
        conn.commit()
        print(f"{len(employees)} employees inserted successfully")
    except Error as e:
        print(f"Error inserting employees: {e}")

def display_all_employees(conn):
    """Retrieve and display all employee records"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        employees = cursor.fetchall()
        if employees:
            print("\n=== All Employees ===")
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Dept: {emp[2]}, Salary: ₹{emp[3]}, Designation: {emp[4]}")
        else:
            print("No employees found")
    except Error as e:
        print(f"Error retrieving employees: {e}")

def search_by_id(conn, emp_id):
    """Search for an employee using Emp_ID"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee WHERE Emp_ID = %s", (emp_id,))
        emp = cursor.fetchone()
        if emp:
            print(f"\n=== Employee Found ===")
            print(f"ID: {emp[0]}, Name: {emp[1]}, Dept: {emp[2]}, Salary: ₹{emp[3]}, Designation: {emp[4]}")
        else:
            print(f"No employee found with ID {emp_id}")
    except Error as e:
        print(f"Error searching employee: {e}")

def update_salary(conn, emp_id, new_salary):
    """Update the salary of an employee"""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Employee SET Salary = %s WHERE Emp_ID = %s", (new_salary, emp_id))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Employee ID {emp_id} salary updated to ₹{new_salary}")
        else:
            print(f"No employee found with ID {emp_id}")
    except Error as e:
        print(f"Error updating salary: {e}")

def update_designation(conn, emp_id, new_designation):
    """Update the designation of an employee"""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Employee SET Designation = %s WHERE Emp_ID = %s", (new_designation, emp_id))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Employee ID {emp_id} designation updated to {new_designation}")
        else:
            print(f"No employee found with ID {emp_id}")
    except Error as e:
        print(f"Error updating designation: {e}")

def delete_employee(conn, emp_id):
    """Delete an employee record"""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Employee WHERE Emp_ID = %s", (emp_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Employee ID {emp_id} deleted successfully")
        else:
            print(f"No employee found with ID {emp_id}")
    except Error as e:
        print(f"Error deleting employee: {e}")

def employees_above_salary(conn, min_salary):
    """Display employees with salary greater than specified amount"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee WHERE Salary > %s", (min_salary,))
        employees = cursor.fetchall()
        if employees:
            print(f"\n=== Employees with Salary > ₹{min_salary} ===")
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: ₹{emp[3]}")
        else:
            print(f"No employees found with salary > ₹{min_salary}")
    except Error as e:
        print(f"Error searching employees: {e}")

def menu(conn):
    """Menu-driven application for CRUD operations"""
    while True:
        print("\n=== Employee Management System ===")
        print("1. Insert an employee")
        print("2. Insert multiple employees")
        print("3. Display all employees")
        print("4. Search employee by ID")
        print("5. Update employee salary")
        print("6. Update employee designation")
        print("7. Delete employee by ID")
        print("8. Search employees by salary")
        print("9. Exit")
        
        choice = input("Enter choice (1-9): ").strip()
        
        if choice == "1":
            name = input("Enter name: ").strip()
            dept = input("Enter department: ").strip()
            salary = float(input("Enter salary: "))
            desig = input("Enter designation: ").strip()
            insert_employee(conn, name, dept, salary, desig)
        
        elif choice == "2":
            num = int(input("Enter number of employees: "))
            emps = []
            for i in range(num):
                print(f"\nEmployee {i+1}:")
                name = input("Enter name: ").strip()
                dept = input("Enter department: ").strip()
                salary = float(input("Enter salary: "))
                desig = input("Enter designation: ").strip()
                emps.append((name, dept, salary, desig))
            insert_multiple_employees(conn, emps)
        
        elif choice == "3":
            display_all_employees(conn)
        
        elif choice == "4":
            emp_id = int(input("Enter Employee ID: "))
            search_by_id(conn, emp_id)
        
        elif choice == "5":
            emp_id = int(input("Enter Employee ID: "))
            new_salary = float(input("Enter new salary: "))
            update_salary(conn, emp_id, new_salary)
        
        elif choice == "6":
            emp_id = int(input("Enter Employee ID: "))
            new_desig = input("Enter new designation: ").strip()
            update_designation(conn, emp_id, new_desig)
        
        elif choice == "7":
            emp_id = int(input("Enter Employee ID: "))
            delete_employee(conn, emp_id)
        
        elif choice == "8":
            min_salary = float(input("Enter minimum salary (₹): "))
            employees_above_salary(conn, min_salary)
        
        elif choice == "9":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Execute the program
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'employee_db'
}

try:
    conn = connect_db(config)
    create_database(conn)
    create_table(conn)
    menu(conn)
    conn.close()
except Exception as e:
    print(f"Connection error: {e}")
    print("Make sure MySQL is running and credentials are correct.")
