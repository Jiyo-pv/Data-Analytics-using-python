# Q25 Library Management System using SQLite - @JIYO P V 2026-09-06
import sqlite3

# Database file
db_file = "library.db"

def connect_db():
    """Establish connection with SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table(conn):
    """Create Books table with constraints"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL,
                Author TEXT NOT NULL,
                Category TEXT NOT NULL,
                Copies INTEGER NOT NULL
            )
        """)
        conn.commit()
        print("Books table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_book(conn, title, author, category, copies):
    """Insert a new book using parameterized queries"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Books (Title, Author, Category, Copies)
            VALUES (?, ?, ?, ?)
        """, (title, author, category, copies))
        conn.commit()
        print(f"Book '{title}' inserted successfully. ID: {cursor.lastrowid}")
    except sqlite3.Error as e:
        print(f"Error inserting book: {e}")

def insert_multiple_books(conn, books):
    """Insert multiple book records using executemany()"""
    try:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO Books (Title, Author, Category, Copies)
            VALUES (?, ?, ?, ?)
        """, books)
        conn.commit()
        print(f"{len(books)} books inserted successfully")
    except sqlite3.Error as e:
        print(f"Error inserting books: {e}")

def display_all_books(conn):
    """Retrieve and display all book records"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        if books:
            print("\n=== All Books in Library ===")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category: {book[3]}, Copies: {book[4]}")
        else:
            print("No books in library")
    except sqlite3.Error as e:
        print(f"Error retrieving books: {e}")

def search_by_id(conn, book_id):
    """Search for a book using Book_ID"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE Book_ID = ?", (book_id,))
        book = cursor.fetchone()
        if book:
            print(f"\n=== Book Found ===")
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category: {book[3]}, Copies: {book[4]}")
        else:
            print(f"No book found with ID {book_id}")
    except sqlite3.Error as e:
        print(f"Error searching book: {e}")

def update_copies(conn, book_id, new_copies):
    """Update the number of available copies"""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Books SET Copies = ? WHERE Book_ID = ?", (new_copies, book_id))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Book ID {book_id} updated. New copies: {new_copies}")
        else:
            print(f"No book found with ID {book_id}")
    except sqlite3.Error as e:
        print(f"Error updating book: {e}")

def delete_book(conn, book_id):
    """Delete a book record using Book_ID"""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Books WHERE Book_ID = ?", (book_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Book ID {book_id} deleted successfully")
        else:
            print(f"No book found with ID {book_id}")
    except sqlite3.Error as e:
        print(f"Error deleting book: {e}")

def search_by_category(conn, category):
    """Display all books of a specified category"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE Category = ?", (category,))
        books = cursor.fetchall()
        if books:
            print(f"\n=== Books in '{category}' Category ===")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Copies: {book[4]}")
        else:
            print(f"No books found in '{category}' category")
    except sqlite3.Error as e:
        print(f"Error searching category: {e}")

def menu(conn):
    """Menu-driven application for CRUD operations"""
    while True:
        print("\n=== Library Management System ===")
        print("1. Insert a book")
        print("2. Insert multiple books")
        print("3. Display all books")
        print("4. Search book by ID")
        print("5. Update book copies")
        print("6. Delete book by ID")
        print("7. Search by category")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ").strip()
        
        if choice == "1":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            category = input("Enter category: ").strip()
            copies = int(input("Enter copies: "))
            insert_book(conn, title, author, category, copies)
        
        elif choice == "2":
            num = int(input("Enter number of books to insert: "))
            books = []
            for i in range(num):
                print(f"\nBook {i+1}:")
                title = input("Enter title: ").strip()
                author = input("Enter author: ").strip()
                category = input("Enter category: ").strip()
                copies = int(input("Enter copies: "))
                books.append((title, author, category, copies))
            insert_multiple_books(conn, books)
        
        elif choice == "3":
            display_all_books(conn)
        
        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            search_by_id(conn, book_id)
        
        elif choice == "5":
            book_id = int(input("Enter Book ID: "))
            new_copies = int(input("Enter new number of copies: "))
            update_copies(conn, book_id, new_copies)
        
        elif choice == "6":
            book_id = int(input("Enter Book ID: "))
            delete_book(conn, book_id)
        
        elif choice == "7":
            category = input("Enter category: ").strip()
            search_by_category(conn, category)
        
        elif choice == "8":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Execute the program
conn = connect_db()
create_table(conn)
menu(conn)
conn.close()
