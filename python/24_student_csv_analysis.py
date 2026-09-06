# Q24 Student CSV Program - Create, Read, Analyze - @JIYO P V 2026-09-06
import csv

def create_student_csv(csv_file="students.csv", data=None):
    """Create students CSV file with sample data"""
    if data is None:
        data = [
            [1, "Alice", 85],
            [2, "Bob", 92],
            [3, "Charlie", 78],
            [4, "Diana", 88],
            [5, "Eve", 95],
        ]
    try:
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll_No", "Name", "Marks"])
            writer.writerows(data)
        print(f"CSV file '{csv_file}' created successfully\n")
    except IOError as e:
        print(f"Error creating CSV: {e}")

def analyze_student_data(csv_file="students.csv"):
    """Read and analyze student data from CSV file"""
    try:
        students = []
        total_marks = 0
        highest_mark = -1
        topper = None
        
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                roll_no = int(row["Roll_No"])
                name = row["Name"]
                marks = int(row["Marks"])
                
                students.append({"roll_no": roll_no, "name": name, "marks": marks})
                total_marks += marks
                
                if marks > highest_mark:
                    highest_mark = marks
                    topper = name
        
        # Display results
        print("=== Student Data Analysis ===\n")
        print("All Students:")
        for s in students:
            print(f"  Roll No: {s['roll_no']}, Name: {s['name']}, Marks: {s['marks']}")
        
        average_marks = total_marks / len(students)
        print(f"\nStudent with Highest Marks: {topper} ({highest_mark})")
        print(f"Average Marks of Class: {average_marks:.2f}")
    
    except FileNotFoundError:
        print(f"File '{csv_file}' not found")
    except Exception as e:
        print(f"Error: {e}")

# Execute the program
create_student_csv()
analyze_student_data()
