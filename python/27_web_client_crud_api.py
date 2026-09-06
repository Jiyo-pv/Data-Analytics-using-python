# Q27 Web Client CRUD Operations using requests module - @JIYO P V 2026-09-06
# Note: Requires requests library. Install: pip install requests
# API: https://crudcrud.com/

import requests
import json

# API endpoint for students resource
API_URL = "https://crudcrud.com/api/97764ca636584b20ab4034340d82f2c6/students"

def create_student(name, age, course):
    """
    Create a new student record via POST request
    Returns the created student's _id
    """
    payload = {
        "name": name,
        "age": age,
        "course": course
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 201:
            student = response.json()
            print(f"✓ Created: {name} (ID: {student.get('_id')})")
            return student.get("_id")
        else:
            print(f"✗ Failed to create student. Status: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"✗ Error creating student: {e}")
        return None

def get_all_students():
    """
    Retrieve all students via GET request
    Returns list of students
    """
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            students = response.json()
            return students
        else:
            print(f"✗ Failed to fetch students. Status: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"✗ Error fetching students: {e}")
        return []

def update_student(student_id, name, age, course):
    """
    Update a student's details via PUT request
    """
    update_url = f"{API_URL}/{student_id}"
    payload = {
        "name": name,
        "age": age,
        "course": course
    }
    
    try:
        response = requests.put(update_url, json=payload)
        if response.status_code == 200:
            print(f"✓ Updated: {name}")
            return True
        else:
            print(f"✗ Failed to update student. Status: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"✗ Error updating student: {e}")
        return False

def delete_student(student_id):
    """
    Delete a student record via DELETE request
    """
    delete_url = f"{API_URL}/{student_id}"
    
    try:
        response = requests.delete(delete_url)
        if response.status_code == 200:
            print(f"✓ Deleted: Student ID {student_id}")
            return True
        else:
            print(f"✗ Failed to delete student. Status: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"✗ Error deleting student: {e}")
        return False

def display_students(students):
    """Display list of students in formatted way"""
    if not students:
        print("No students found")
        return
    
    print("\n=== All Students ===")
    for i, student in enumerate(students, 1):
        print(f"{i}. Name: {student.get('name')}, Age: {student.get('age')}, Course: {student.get('course')}, ID: {student.get('_id')}")

# Execute the program
print("=== Student Management via REST API ===")
print("\n1. Create new students:")
student1_id = create_student("Alice Johnson", 20, "Data Science")
student2_id = create_student("Bob Smith", 22, "AI")
print(f"Created students with IDs: {student1_id}, {student2_id}")

print("\n2. Display all students:")
students = get_all_students()
display_students(students)

print("\n3. Update student:")
if students:
    first_student = students[0]
    update_student(first_student['_id'], "Updated Name", 21, "Computer Science")
    print("Student updated")

print("\n4. Display all students after update:")
students = get_all_students()
display_students(students)

print("\n5. Delete a student:")
if student1_id:
    delete_student(student1_id)
    print(f"Deleted student with ID: {student1_id}")

print("\n6. Final student list:")
students = get_all_students()
display_students(students)
