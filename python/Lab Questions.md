1. Check whether the given string can be used as a valid variable name in Python.  
   **Explanation:**  
   In Python, a valid variable name:  
* Can only contain letters (a–z, A–Z), digits (0–9), and underscores (\_).  
* The variable name cannot begin with a digit.  
* The string cannot contain reserved keywords such as "for," "if," "class," and so on.


2.  We provide you with a list of integers. In this list, every number appears **twice**, except for one number that appears **only once**. Your task is to find that single, unique number.

   **Example:**

   If the list is \[4, 1, 2, 1, 2\], the unique number is 4\. If the list is \[7, 3, 5, 4, 5, 3, 4\], the unique number is 7\.

   **Constraints:**

   You should try to solve this with a time complexity of O(n) (linear time).

   You should try to solve this without using extra space (O(1) space complexity), meaning no additional data structures like hash maps or sets.

   

3. Write a Python program that defines a function named process\_string() that:  
* Accepts a string input from the user.  
* Prints the string in uppercase and lowercase.  
* Displays the length of the string.  
* Reverses the string using slicing and prints the result.  
* check whether the given string is palindrome or not

             Then, call the function to execute these operations.

**Note on Slicing**

String slicing in Python is a way to extract a portion of a string by specifying a start and end index. It uses the format string\[start:end\], where: 

Start is the index where slicing begins (inclusive).

end is the index where slicing ends (exclusive).

If start is omitted, it defaults to the beginning of the string. If end is omitted, it defaults to the end of the string. 

Negative indices can also be used: \-1 is the last character, \-2 is the second to last, etc.

A third optional parameter, step, can be added to control the characters included in the slice. For example, string\[start:end:step\]. A step of 2 would select every second character, while a step of \-1 would reverse the string.

4. Write a menu-driven program that performs the following operations on strings:  
   *   Check if the string is a substring of another string.  
   *  Count Occurrences of Character  
   *  Replace a substring with another substring  
   *  Convert to Capital Letters  
5. Build a menu-driven application that uses the data structure dictionary to create, update, search, and delete phonebook entries.   
6.  Create a simple calculator in Python.   
7. You are managing a conference with multiple sessions.  
    You have the following data:  
* Set A: Registered attendees for the **"AI & Data Science"** session  
* Set B: Registered attendees for the **"Cybersecurity"** session

  Write a Python program to: 

* Collect input from the user.   
* List **all unique attendees** (those who registered for any session)  
* List **attendees who registered for both sessions**  
* List attendees who registered **only for "AI & Data Science."**  
* List attendees who registered **only for "Cybersecurity."**


**Question 8: Number Analyzer Challenge**

Your task is to develop a program that performs a comprehensive analysis of an integer provided by the user. For a given input number, your program should determine and clearly state whether it exhibits the following properties.

Important: For each property, you must implement a separate function to perform the check.

* Even or Odd: Is the number perfectly divisible by two?  
* Palindrome: Does the number read the same forwards and backward (e.g., 121, 343)?  
* Armstrong: Is the number equal to the sum of its own digits, each raised to the power of the number of digits (e.g., for a 3-digit number like 153, it's 1+125+27=153)?  
* Prime: Is the number a natural number greater than 1 that has no positive divisors other than 1 and itself (e.g., 2, 3, 5, 7, 11)?  
* Perfect: Is the number a positive integer that is equal to the sum of its proper positive divisors (i.e., its divisors excluding the number itself, e.g., 6 because 1+2+3=6)?

**Question 9: Dynamic Greeting Generator (Variable-Length Arguments)**

* **Scenario:** You want to create a greeting system that can greet a single person or a group of people.  
* **Task:**  
  1. Define a function `greet_people()` that can accept any number of name arguments.  
  2. Inside the function, if no names are provided, print "Hello, stranger\!"  
  3. If one name is provided, print "Hello, \[Name\]\!"  
  4. If multiple names are provided, print "Hello, \[Name1\], \[Name2\], and \[Name3\]\!" (Adjust for any number of names).  
  5. Test your function with:  
     * `greet_people()`  
     * `greet_people("Alice")`  
     * `greet_people("Bob", "Charlie")`  
     * `greet_people("David", "Eve", "Frank")`


**Question 10: Password Strength Checker ()**

* **Scenario:** You're developing a simple password strength checker.  
* **Task:**  
  1. Prompt the user to enter a password.  
  2. Implement the following conditions for password strength:  
     * At least 8 characters long.  
     * The password must contain at least one digit.  
     * The password must contain at least one uppercase letter.  
     * The password must contain at least one lowercase letter.  
     * The password must also include at least one special character.  
  3. Print "Strong Password" if all conditions are met; otherwise, print "Weak Password" and indicate which conditions are missing.

**Question 11: Recursive Functions \- Sum & Factorial**

**Task**: Implement two recursive Python functions for a given non-negative integer n:

* Calculates the sum of all natural numbers from 1 to n.  
* Calculates n\!.

**Test your functions with:**

* n=5  
* n=10  
* n=18

**Question 12: Modular Text Analysis Toolkit**

**Task:** Build a text analysis toolkit using Python modules.

**Structure:**

your\_project\_folder/

├── text\_preprocessor.py

├── text\_analyzer.py

└── main\_analyzer.py

**Module Specs:**

1. **text\_preprocessor.py**:  
   * normalize\_text(text): lowercase, remove punctuation.  
   * tokenize\_text(text): split into words.  
2. **text\_analyzer.py**:  
   * word\_frequency(word\_list): count word occurrences.  
   * character\_count(text): count alphabetic chars.  
   * unique\_word\_count(word\_list): count unique words.  
3. **main\_analyzer.py**:  
   * Import and use functions from other modules.  
   * Prompt for text.  
   * Display: Original, Normalized, Tokens, Word Frequency, Total Char Count, Unique Word Count.  
   * Print docstring of the functions

**Requirements:** Modularity, proper imports, docstrings, type hinting, readable code.

**Question 13:**

Create a class Student with attributes name, roll\_number, and course. Define an \_\_init\_\_ method to initialize these attributes and a method display() to print them.

**Question 14:**

Define a class Circle with attribute radius. Create a method get\_area() to return the area and another method get\_circumference() to return the circumference.

Formula:

Area \= π × radius²

Circumference \= 2 × π × radius

**Question 15:**

Create a class Employee with attributes emp\_id, name, basic\_pay. Add a method calculate\_salary() that calculates gross salary as:

Gross \= Basic Pay \+ HRA (20%) \+ DA (10%).

Then display the salary details.

**Question 16:**

Create a class SmartCalculator that demonstrates simulated method overloading using different approaches:

* Implement a method add() that:


  * Adds two numbers if two are given.  
    * Adds three numbers if three are given (use default arguments).  
        
  * Implement a method multiply() that:  
    * Accepts any number of arguments using \*args and returns their product.

    

  * Implement a method process() that behaves differently based on the type of the argument:

    

    * If the argument is a string, print it in uppercase.  
    * If the argument is a list of numbers, print the sum of the numbers.

  Finally, create objects of the class and demonstrate all three features with suitable examples.


  

**Question 17:**  
Create a class ComplexNumber with attributes real and imag.

* Overload the \+ operator to add two complex numbers.  
* Overload the \== operator to check if two complex numbers are equal.  
* Demonstrate these operations using suitable examples.  
  


  
**Question 18:**

* Create a class Vehicle with attributes brand and model and a method display\_info() that prints these details.  
* Derive a class Car that adds an attribute seating\_capacity and overrides display\_info() to include this extra detail.  
* Create objects of both classes and demonstrate how method overriding works.  
* Use super() in the derived class to call the base class method before adding extra information.


**Question 19:**   
**Read and Analyze Text File**  
Write a program to read a .txt file and:

* Count the number of lines, words, and characters.  
* Display the top 5 most frequent words with their frequencies.  
* Handle file not found and permission errors.


**Question 20:**   
**Custom Exception: Invalid Age**  
Write a class InvalidAgeException that inherits from Exception.

* Create a function that accepts user input for age and throws the exception if the age is not between 18 and 60\.  
* Handle the exception and display appropriate messages.


**Question 21: Try-Except-Else-Finally Flow Demonstration**  
Write a program where:

* You simulate a transaction (like withdrawing money from an account).  
* Demonstrate use of try, except, else, and finally blocks clearly.


**Question 22: Date Format Converter**  
Write a program that:

* Accepts a date in dd-mm-yyyy format.  
* Converts and displays it in MonthName dd, yyyy format.  
* Handles exceptions for invalid date formats or out-of-range values  
  

**QUESTION 23: CSV Data Analysis**  
Write a program to read a CSV file containing rainfall data with columns: Date, Station, and Rainfall (mm). Using NumPy, compute:

* Average rainfall per station  
* Maximum rainfall recorded and the date  
* Standard deviation of rainfall  
* Finally, save the computed results into a new CSV file.

\[Use the CSV library.\]

**Question 24:**  
Write a Python program that does the following:

* Create a CSV file named students.csv with the following columns:Roll\_No, Name, Marks  
* Insert at least 5 student records into	 the file.  
* Read the data from the CSV file and display:  
* The student with the highest marks.  
* The average marks of the class.

**Question 25:**  
Develop a Library Management System using Python and SQLite to manage the details of books available in a library.  
**Table: Books**

| Field Name | Data Type | Constraint |
| ----- | ----- | ----- |
| **Book\_ID** | **Integer** | **Primary Key, Auto Increment** |
| **Title** | **Text/VARCHAR(100)** | **NOT NULL** |
| **Author** | **Text/VARCHAR(100)** | **NOT NULL** |
| **Category** | **Text/VARCHAR(50)** | **NOT NULL** |
| **Copies** | **Integer** | **NOT NULL** |

1. Write a Python program to establish a connection with an SQLite database.  
2. Write a Python program to create the Books table with appropriate constraints.  
3. Write a Python program to insert a new book into the Books table using parameterized queries.  
4. Write a Python program to insert multiple book records using the executemany() method.  
5. Write a Python program to retrieve and display all book records from the database.  
6. Write a Python program to search for a book using the Book\_ID.  
7. Write a Python program to update the number of available copies of a book using the Book\_ID.  
8. Write a Python program to delete a book record using the Book\_ID.  
9. Write a Python program to display all books belonging to a specified category entered by the user.  
10. Write a menu-driven Python application to perform all CRUD operations on the Books table.

**Question 26:**  
Develop an Employee Management System using Python and MySQL to maintain employee information.

**Table: Employee**

| Field Name | Data Type | Constraint |
| ----- | ----- | ----- |
| **Emp\_ID** | **Integer** | **Primary Key, Auto Increment** |
| **Name** | **Text/VARCHAR(100)** | **NOT NULL** |
| **Department** | **Text/VARCHAR(100)** | **NOT NULL** |
| **Salary** | **DECIMAL(10,2)/REAL** | **NOT NULL** |
| **Designation** | **Text/VARCHAR(100)** | **NOT NULL** |

1. Write a Python program to establish a connection with an MySQL database.  
2. Write a Python program to create the Employee table with appropriate constraints.  
3. Write a Python program to insert a new employee record using parameterized queries.  
4. Write a Python program to insert multiple employee records using the executemany() method.  
5. Write a Python program to retrieve and display all employee records.  
6. Write a Python program to search for an employee using the Emp\_ID.  
7. Write a Python program to update the salary of an employee using the Emp\_ID.  
8. Write a Python program to update the designation of an employee using the Emp\_ID.  
9. Write a Python program to delete an employee record using the Emp\_ID.  
10. Write a Python program to display the details of employees whose salary is greater than ₹50,000.  
11. Write a menu-driven Python application to perform all CRUD operations on the Employee table.

**Question 27:**

Write a Python program that implements a **web client** using the `requests` module to interact with a `students` resource hosted on [**https://crudcrud.com**.](https://crudcrud.com) The program should be organized using **functions** (not a class) and should:

1. Define a function `create_student(name, age, course)` that sends a **POST** request to add a student and returns the created student's `_id`.  
2. Define a function `get_all_students()` that sends a **GET** request and returns the list of all students.  
3. Define a function `update_student(student_id, name, age, course)` that sends a **PUT** request to update a student's details.  
4. Define a function `delete_student(student_id)` that sends a **DELETE** request to remove a student.  
5. In the main part of the program:  
   * Create 3 student records using `create_student()`.  
   * Print all students using `get_all_students()`.  
   * Update the course of the 2nd student.  
   * Delete the 1st student.  
   * Print the final list of students.  
6. Check the `status_code` of each response and print whether the operation was **successful** or **failed**.  
   

**Question:28**  
Create a Login form using CGI and display the input on a different page.  
**Question:29**  
Create a registration form for MSc admission and display the inserted data on the web page.  
**Question:30**  
Create a MySQL/Sqllite database and perform INSERT, UPDATE, DESTROY, and SELECT (display) operations using the CGI interface.

**Question 31:**  
Write a Python program using NumPy to:

* Create a 1D array of numbers from 1 to 20\.  
* Reshape it into a 4×5 matrix.  
* Find the transpose of the matrix.  
* Calculate the sum of all elements, row-wise sum, and column-wise sum.  
* Extract all even numbers from the array using Boolean indexing.

**Question 32:**  
Create a 5 × 5 NumPy array with numbers from 1 to 25\. Then do the following using slicing:

* Print the center 3 × 3 part of the array.  
* Print the reverse of the center 3 × 3 part.  
* Print the first 2 rows and last 2 columns.  
* Print all elements of the array in a single line,

**Question 33:**  
Create individual Pandas Series for storing the details of 5 students:

*     Name, Age, Course, and Marks. Convert these Series into a DataFrame.  
*     Add a new column to categorize students as Pass (marks ≥ 40\) or Fail (marks \< 40).  
*     Display only the students who passed.


**Question 34:**  
Create a Pandas DataFrame to store details of employees:

*     EmployeeID, Name, Department, Salary.  
*     Compute the average salary per department.  
*     Identify the employee with the highest salary.

**Question 35:**  
Create a DataFrame to store monthly sales of three products (Product A, Product B, Product C) across 6 months.

*     Find the month with highest total sales.  
*     Plot a bar chart comparing sales of all three products.  
  


**Question 36:**  
Create a DataFrame to store weather details for 7 days:

*     Day, Temperature (°C), Humidity (%), Rainfall (mm).  
*     Compute the average temperature and total rainfall.  
*     Plot a line graph of Temperature vs. Day.

**Question 37:**  
Write a Pandas program to convert continuous values of a column in a given data frame to categorical.  
Input:  
{ 'Name': \['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'\], 'Age': \[18, 22, 40, 50, 80, 5\] }

**Question 38:**  
Write a Pandas program to join the two given data frames along rows and assign all the data.  
***student\_data1:***

|  | student\_id | name | marks |
| :---- | :---- | ----- | :---- |
| 0 | s1 | Danniella Fenton | 200 |
| 1 | s2 | Ryder Storey | 210 |
| 2 | s3 | Bryce Jensen | 190 |
| 3 | s4 | Ed Bernal | 222 |
| 4 | s5 | Kwame Morin | 199 |

***student\_data2:***

|  | student\_id | name | marks |
| :---- | :---- | ----- | :---- |
| 0 | s4 | Scarlette Fisher | 201 |
| 1 | s5 | Carla Williamson | 200 |
| 2 | s6 | Dante Morse | 198 |
| 3 | s7 | Kaiser William | 219 |
| 4 | s8 | Madeeha Preston | 201 |

**Question 39:**  
Write a Pandas program to join the two given data frames along columns and assign all the data. (Use the same dataset as above.)  
**Question 40:**  
Write a Pandas program to join the two given data frames along rows and merge with another data frame along the common column id.   
***exam\_data:***

|  | student\_id | exam\_id |
| ----- | :---- | ----: |
| 0 | S1 | 23 |
| 1 | S2 | 45 |
| 2 | S3 | 12 |
| 3 | S4 | 67 |
| 4 | S5 | 21 |
| 5 | S7 | 55 |
| 6 | S8 | 33 |
| 7 | S9 | 14 |
| 8 | S10 | 56 |
| 9 | S11 | 83 |
| 10 | S12 | 88 |
| 11 | S13 | 12 |

(Add this data to the above dataset.)  
**Questions 41:**  
Write a Pandas program to join the two data frames with matching records from both sides, where available. (Same dataset as above.)

**Questions 42: Pandas Grouping**

Write a Pandas program to split the following data frame into groups based on school code. Also, check the type of GroupBy object.get the mean, min, and max values of age for each school.

|  | school |  class |  name |  date\_Of\_Birth |  age |  height |  weight |  address |
| ----- | ----- | :---- | :---- | ----- | ----- | :---- | :---- | :---- |
|  S1 |  s001 |  V |  Alberto Franco |  15/05/2002 |  12 |  173 |  35 |  street1 |
|  S2 |  s002 |  V |  Gino Mcneill |  17/05/2002 |  12 |  192 |  32 |  street2 |
|  S3 |  s003 |  VI |  Ryan Parkes |  16/02/1999 |  13 |  186 |  33 |  street3 |
|  S4 |  s001 |  VI |  Eesha Hinton |  25/09/1998 |  13 |  167 |  30 |  street1 |
|  S5 |  s002 |  V |  Gino Mcneill |  11/05/2002 |  14 |  151 |  31 |  street2 |
|  S6 |  s004 |  VI |  David Parkes |  15/09/1997 |  12 |  159 |  32 |  street4 |

**Questions 43: Pandas Grouping**  
Write a Pandas program to split the following data frame into groups based on all columns and calculate groupby value counts on the data frame.  
***Test Data:***

|  | *Id* | *type* | *book* |
| :---- | :---: | :---- | :---- |
| *0* | *1* | *10* | *Math* |
| *1* | *2* | *15* | *English* |
| *2* | *1* | *11* | *Physics* |
| *3* | *1* | *20* | *Math* |
| *4* | *2* | *21* | *English* |
| *5* | *1* | *12* | *Physics* |
| *6* | *2* | *14* | *English* |

**Question 44:**  
Visualize the following using the given dataset ([alphabet\_stock\_data.csv](https://drive.google.com/file/d/14EKuNW4qoH3KUOWkkn3qSuG2nwwPtYCC/view?usp=drive_link)),

1. Create a line plot of the historical stock prices of Alphabet Inc. between two specific dates.  
2. Create a bar plot of the trading volume of Alphabet Inc. stock between two specific dates.  
3. Create a stacked histogram plot with more bins of opening, closing, high, and low stock prices of Alphabet Inc. between two specific dates.  
4. Create a scatter plot of the trading volume/stock prices of Alphabet Inc. stock between two specific dates.

**Question 45:**  
Write a Python program to create multiple plots as in the screenshot (use any method).

**Question 46:**  
Write a Python program to create a bar plot from a data frame. Sample Data Frame:  
a b c d e  
2 4,8,5,7,6  
4 2,3,4,2,6  
6 4,7,4,7,8  
8 2,6,4,8,6  
10 2,4,3,3,2  
Create the code snippet which gives the output shown in the following screenshot:  
![][image1]  
**Question 47:**  
Handle the given dataset ([Data.csv](https://drive.google.com/file/d/1oTdtc4-tUx9IE-J7U1s_hkRw2OPRJCn6/view?usp=drive_link)) with adequate preprocessing steps  
mentioned and visualize the dataset with appropriate graphs.

* Handle Missing Data Values  
* Encode the categorical data  
* Scale your features

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZgAAAFJCAIAAAApO6yIAABRL0lEQVR4Xu19DaxlZXX2ngEGCqSGwfYK2GSEgrSVAafahiG9jgXJYDPfVKRDblUU04x1dKT9OkVEnGwkBn/6O5AQLEQJt0CrrdQ2BVLNtWraGr+pJo3Kj2mZ1EgoYqg6Vkvgfnuttc97373W++5Za/+cs8+e98mC7POedfd51nrWfs4+c/fdJ1tdXb3yyitf/OIXn3vuuT/84Q9XExISEuYN2Qc+8IFvfOMb9GD9+vXPPPNMNSEhISFh6Miuu+66p59+mh4ce+yx6aQsISFh7pAV/5144onr1q0rTsf4kwkJCQnzgOzee+/99re/TQ9OOumk7373u+65p5566otf/OLBhISEhKGi8KjCqbLFxUXnXMVJ2Wc/+1n3cHl5OTsjK+PCLFuaVrxNrKQYTSRxRxzTFPfCiTWdkYFT7dix47HHHiPnOvbYY5944glnZGR47qHDOeecw5dq4ednBfJQZJl7rYUtCy5fgzZ8EhiszbHma8QthuH27PaVbKWIF2cvpo1ipVjnqQJWPlMDjPjtt2Mp1bj99uBR1geszbHma8T1Yd1/MJ9sKvv85z+/sLBw0003XXbZZW9729tkhr9CuOeee/hSLfz8PoysDZ8EBmtzrPkacX0juyG7wWRkVj5TwxCMzNoca75GXB/W/QfzSyPjyx5iRtYGfRhZwhxBI65vZC6URjZYDMHI+oZG3M7R3MieeuopvlQLP19jZFveucXla9CGTwKDtTnWfI24vpHdn91vMjIrn6lhCEZmbY41XyOuD+v+g/nNjSy4WAM/X2NkO+7Z4fI1aMMngcHaHGu+RlzfyPwNjZFZ+UwNQzAy6wtZ8zXi+rDuP5iPLtXIyNqgDyNLmCNoxPWNzIXSyAaLIRhZPQ4dOnTiiScCzwGjYFjw9GknI0uYATTiZsnIZgGwAzwMhwzfKBxtWPeXGCiDr66u7tmzhy/Vws8HOaWL5bDsXksz6z7a8ElgsDbHmq8RFw75iZHtzHaajMzKZ2qAEZ+1kdU3h2yCrw4MvlEQmhtZG4Cc0sVyWG5sZAlzBI24cMinM7KpIxmZASCndLEclpORHQ3QiAuHfDKyqSMZmQEgp3SxHJaTkR0N0IgLh3wysqnjqDOyhx56iC/Vws8HOaWL5bDc2Mja8ElgsDbHmq8RFw75iZF9OPuwycisfKYGGPFZG1l9c5iRHTp06IQTuvwlJvttYzNkHRpZG0BBeShaGFnCHEEjbpbOyGYBZmT0sFjoKLoxE98oCMnIEmYAjbhZMrJZYOZG9rGPfezMM8/8iZ/4iYsuumh5eZk/jfCNgqAysoWFhR07YPJ27dr1qU99itZPP/102tizZ88dd9xB20Wa+wOCD37wg27xG9/4RvGzxfa+fftWSc5zsuzqiX9dsGZkf/AHf0A/5f/FlnX/tPiFL3yBtt/ylrfQRgHJf1W3f9rW7586Rmiw/8OHD89w/0Uz9fsvPixs376dtpX7L4zsiPuHQx6N7L7svldmr6Qj/jXZa+gwq99/jH8xzEH+1v6sRvp/xP3DiJORPfBAduBA6WLbtzsjc/v3PwDq96/hT0dKbP+f+cxnqMNuBThzP2ocRzayf//3f6eNZ5999uKLL3b3SfRRELr11lvdw/PPP39xcfHIRnbE17YCOkPOxSKdkR0d0IibpTOyWYCciz0UftQ4bGby13/913fffTdfbXxGZnptDaAzzrz8SEZ2dEAjbpaMbBaYuZGdeuqpr371q6+55pobb7zx6quvLv7PM5KRJQwEGnGzZGSzwMyNzP/akHvvvbd3Iwve3qwG1hsrambdRxs+CQzW5ljzNeJmnpGlGyt2iPrmDMfIHnzwwWOPPbZ3I2sD6IwzLz9aGFnCHEEjbpbOyGaBmRvZ8ccf/4Y3vOHaa6895phjlpaWkpElDBcacbNkZLMAM7LxXxDr//pZAz8fCspD0cLI2vBJYLA2x5yvEDfzjGxrttVkZFY+UwOM+KyNrL45zMiGCd8oCCojC15H9trXvpY2lNeRHT58eLXP68j8/dNi7Doa2nD8V3X7p239/v1xabD/muuAaKPX/RfP6vdfvMf+67/+K20r92+9juyj2UfpiFdeRxbjf7CL67Boo9n+14xsdteR0ZES2z+7jmyYyNJ1ZAlDgEZcOOTTR8upA+xg8B32jYJANlXHOxlZQufQiAuHfDKyqeOoM7IDBw7wpVr4+SCndLEclhsbWRs+CQzW5ljzNeLCIT8xsr3ZXpORWflMDTDiszay+uYcdUbWBiCndLEclhsbWcIcQSMuHPLpjGzqSEZmAMgpXSyH5WRkRwM04sIhn4xs6jjqjMz/rY0Gfj7IKV0sh+XGRtaGTwKDtTnmfIW4cMinyy96QH1zjjojs17Y5ueDnNLFclhubGRt+CQwWJtjzdeIC4f8xMjuy+4zGZmVz9QAIz5rI6tvjjSyIp9MoBP4ew7i8ccfv/rqq/lqFb5REGjndZOhfHkTQE7pYjksu9fSzHrCnEIjLhzy6aPl1AF24HWYHma7O4rLuQFJJCNLmBtoxIVDPhnZ1BE2MnmoNovd3IAkWhnZW97ylnUTrF+/3r8rY8zI9u/fz5dq4ecXPHiFFC2MrA2fBAZrc6z5GnEzz8iuyq4yGZmVz9QAIz5rI6tvzhCM7FWvetUpp5xy/fXXF452zDHH/OVf/iXLyWJG9i//8i9/jlheXj7vvPNkhr/SHgUPXiFFCyNLmCNoxM3SGdksMAQjK86l3v3ud9PD4447buPGjdWUuJG5x29/+9vZvwUmI0voHBpxs2Rks8AQjOziiy92Dz/+8Y8XHxO95wHZEY1M/kzMyOp/iSuRLr+YI1ibY85XiJulyy/6QX1zRmJkxx9/vPcsIGZkwcUa+PkFD14hRQsja8MngcHaHGu+RtzMMzJ/I1MYmZXP1AAjPmsjq38hsINZG9kpp5zygx/8gB6++c1v9m9+Tcjqjezuu++W/65WPL3xvI0LWxaK2PLOLcUIto9sSVRIsZQt3rZIOQsfWXD56994DPyIiGL9kjsvkftPMaso5Fj/hvVSKRDrDeudWE5cyI+IW8Tmpc1bl7b6UawU6/J15yWgrps3Z7ds5XHzZjf5s41f+cCvZLM2sm3btm3cuPE973lP4WLHHnvsJz7xCZaTZVnBs2BbOBJZU+FRa0a2ffv2//mf/6n+SPSMrA0KHrxCisgZGTxRvI/JEMacMFuUcy8vINodFrfMl8qiuO5EzIXyjGywKIud6RlZPUgR9pBL2Th015G99a1vffjhhwsvO+mkk/7hH/6BZ9Sfkd1yyy3yFG41bmR79uzhS7Xw86E1eShCs17mS+2L8PLb8ElgsDbH5ZdzL5WNiFvmS2VRXGdkO7OdtKE0Miv/qQGKnbWR1TeHFPFXpnxlvwb+LBFo58D7wgsvPO200/znCB2+vAPI6Y+4i9Csl/lSe5z1zrkltAEMk0XcMl8qi+KmM7LpgxThqwODP0uENSOLIRlZgh7JyOoBxSYjaw1/lgjNjaz+l7gSbS6/gCek9isVI2vDJ4HB2hyX35ORpcsvOkR9c446I/O/vEADPx/k9EfcRWjWy3ypPc66y2/DJ4HB2hyX35ORfTj7MG0ojczKf2qAYmdtZPXNOeqMrA1ATn/EXYRmvcyX2uOsd84toQ16MjIXSiMbLKDYWRtZPcZsZMGvg3MnqMqvg6PtZl8HtzbrW7dm999fbu/eTfXI/a/ii8a+DssluEUrf1rsdf81X+dFG8PZv/91ZG9605tArELK64W+KBb7OrjSyPbtC+g7MbL7svvuyu6iI175dXCrEf4Hu/g6Ndpotn8oloxsdl8HRxux/R91XwdXmBpfqoWfX866jNCbdpnvv3258PLb8ElgsDbH5ZfGJJWNiFvmS2VRXHdGti3bRhvKMzIr/6kBip31GVl9c0gRvjow+LNEIJuq4x0zsjYAOf0RdxGa9TJfao+z3jm3hDboychcKI1ssIBiZ21k9UhGZgDI6Y+4i9Csl/lS+5VkZINDMrJ6QLFzZWTF59YTTzgBaHeE+httK5GJA7+5kfkfvDXw86GgPBShWS/zpfYrFSNrwyeBwdocl9+TkW3PttOG0sis/KcGKHbWRlbfHGZk5cOO4qAwoGbwZ4lANlU3GZTBV1dX77nnHr5UCz8f5HTz7Udo1st8qT3OustvwyeBwdocl18ak1Q2Im6ZL5VFcZ2R3ZDdQBtKI7Pynxqg2FkbWX1zSBH+sKNQGtmuXbvOOOOM00477dJLL+XPIfxZIpBN1U0GZfDVdgA53Xz7EZr1Ml9qj7PeObeENiiNSSobEbfMl8qiuOmj5fRBivCHHYXGyI477jj3S9gY/FkikE3VTQZl8NV2ADndfPsRmvUyX2pfhKgnYbYojUkqGxG3zJfKorjJyKYPUoQ/7Cg0Rha8dQWDP0sEsqm6yaAMvlq9jkYDPx/kdPPtR2jWy3ypfRF+fgs+CQzW5rj80pikshFxy3ypLIrrjCz9iVKHqG8OKcIfdhRDNLLDhw/zpVr4+SCnm28/QrNe5kvtcdZdfhs+CQzW5rj80pikshFxy3ypLIrrjOyB7AHaUBqZlf/UAMXO2sjqm0OK8IcdxRCNrA1ATjfffoRmvcyX2uOsd84toQ1KY5LKRsQt86WyKG76aDl9kCL8YUehMbLjjjvu61//Ol+twp8lAtlU3WRQBl/1/hhCCT8f5HTz7Udo1st8qX0RXn4bPgkM1ua4/NKYpLIRcct8qSyK64zsyuxK2lAamZX/1ADFztrI6ptDirCHYEBdxHLGDSiIK664YmFh4Ywzzrjsssv4cwh/lghkU3WTQRl8dXX1wIEDfKkWfj7I6ebbD4+f1cja8ElgsDbH5ZfGJJWNiFvmS2VRXGdke7O9tKE0Miv/qQGKnbWR1TeHFHEPx39BbBtAQXkoQrNe5kvtcdY755bQBj0ZmQulkQ0WUOysjawezMiGCX+WCMnIErpEMrJ6QLHJyFrDnyWCysiCt/EpFmlDeRsf2kN/t/Hx97+KL1p/GxPHf/VIt6mh/dO2fv/+L7kb7P+It2Hpdf87EG6xfv/Fh4Vt27bRdk+38bkgu4COeOVtfGL8D3Z3G5xm+4diZ30bH2Ie2/9Rdxsf62ddP7+cdRmhN+0y33/7cuHlt+GTwGBtjssvjUkqGxG3zJfKorjujKzwMtpQnpFZ+U8NUOysz8jqm0OK8NWBwZ8lAtlUHe+YkbUByOmPuIvQrJf5Unuc9c65JbRBT0bmQmlkgwUUO2sjq8dRZ2TuzFYJPx/k9EfcRWjWy3yp/UrFyNrwSWCwNsfl92Rku7PdtKE0Miv/qQGKnbWR1TfnqDOy/fv386Va+Pkgpz/iLkKzXuZL7XHWXX4bPgkM1ua4/J6M7KrsKtpQGpmV/9QAxc7ayOqbc9QZWRuAnP6IuwjNepkvtcdZ75xbQhv0ZGQulEY2WECxszayeiQjMwDk9EfcRWjWy3yp/UoyssEhGVk9oNh5M7JDhw6RCXQCf88avOQlL+FL3RqZ/+tnDfx8kNMfcRehWS/zpfYrFSNrwyeBwdoclw/DZBG3zJfKorjOyNLdLzpEfXNIEfYQOHcS119vLbNLIwteR7a4uEgbyuvI6IX7u47M3/8qvmjsOhracPxXj3SdFO2ftvX798elwf5rrgOijV73T111i/X7L96xP/nJT9J2T9eR3ZjdSEe88jqyGP+DXVyHRRvN9g/F3j7j68johWL7Z9eRlQL5ntsm7H4dM7LOriNrA2hNHorQm3aZL5uyUjkjSxgCyrmXykbErTtO0kfLWYAUYQ8528ahKPNd73rXGWeccc0115x99tmvfOUrY0bG9kM2VTcZlMFX2wFaQ8PNIjTrZb5sykoyssGhnHupbETcuuMkGdksQIqwh5xt41CUuW7dumeeeabY+PGPf3zhhReajez4448vfqw4yXz3u98tM/wVQvGJki/Vws+H1tBwswjNepkvm7JSMbI2fBIYrM1x+eXcS2Uj4tYdJ56R7cx20obSyKz8pwYodtZGVt8cUoQ95Gwbh6JM/8aKzz33nM3IbrvttkceeaR4/Pzzz/tPuwy22BLQGhpuFqFZL/NlU1bSGdngUM69VDYibt1xks7IZgFShD3kbBuHosxWRnbFFVd85jOfeelLX3ryySf/6Ec/khn+SntAa2i4WYRmvcyXTVlJRjY4lHMvlY2IW3ecJCObBUgR9pCzbRyKMn0jW1lZsRnZWWed9Y53vIOWih1985vfZBnuoYP/WxsN/HxoDQ03i9Csl/myKSsVI2vDJ4HB2hyXX869VDYibt1xki6/6Af1zSFF2EPOtnEoynzXu951+umnF///2Z/92V/6pV+yGdnLXvYy98vadevW3X333SzDPXTwf32rgZ8PraHhZhGa9TJfNmUFZn15eZkY3nrrrbRRoP7v+wlW/kNA7NJEntca1ua4/IP9GNmHsw/ThtLIrPwbI6bIwYgoUGzEyNwk+9BMshX1zTkYNDJ5RViz0F1H9vM///MnnHDC3r17v/e975155pn86Roje8973lOcxdFSYWT33nsvy3APOwG0hoabRWjWy3ypPc769dn1oluqWZ870EjJYosOdC5QY5RzL5WNiFvmS2VR3NsH/9ESyF+eZbtFXM6PtLX820NG9t73xiY5uJ/+QIr4KzVm3QD+nhtDtoV2nn3lK1954xvfSEsbNmx44oknWIZ72AlAzjwUoVkv86X2K+FZL4IpMQ6ATkUbRLFFBzoXqDGIJJc1Lm6Zz2vCCIk7RCPbLSrNYTEoCuRHjEwWu4KTHNxPfyBF+OrAINtCNgW83//+9xcfR8855xz/aZfBFlfxKn++VAs/H+SU2uewLGe9zOcSY3izvi3b5svvfjYGK/+ZgyZMtKAXI7M2x+WXxiSVjYhb5vOaMELiKo3Myr8xgPy8GVl9c0gRvjowyLaQTdXxpgy+2g4gp9Q+h2U562U+lxgj9KZN8rufHQ1owmSxfRhZY5TGJJWNiFvm85owQuIqjWxqAPLzZmT1IEX46sAg20I2VcebMvhqO4CcUvscluWsl/lcYozQrJP87mdHA5owWWwyshkCyCcjmzpkW8im6nhTBl+t/iWqBn4+yCm1z2FZznqZzyXG8GZ9e7bdl9/9bAxW/jMHTZhoQS9GZm2Oyy+NSSobEbfM5zVhhMRVGpmVf2MA+XkzsvrmkCJ8dWCQbSGbquNNGXx1dfWee+7hS7Xw80FOqX0Oy3LWy3wuMYY36zdkN/jyu5+Nwcp/5qAJEy3oxciszXH5pTFJZSPilvm8JoyQuEojs/JvDCA/b0ZW3xxShK8ODLItZFN1vA9GbuPjLqtT3saHtju/jU8h/9Zs613ZXST8ldmVJP+Onm+z0/f+5W1YaMJuym6iSv1rRN/3vvdRZpv9Exrw928j09NtfJy+ytv4rEb4H+ziNji0QfsH8sUY/p81/8p+v9zYu3cvZapu4zMxMqcvXTpHTeuDv/I2PsNENr7b+MTex9zPjgZ0zMti+zgja4zSmKSyEXHLfF4TRkhc5RnZ1ADk5+2MrB6kCF8dGGRbyKbqeFMGX62+42ng54OcUvscluWsl/lcYgxv1t0ZCsnvfjYGK/+ZgyZMtKAXI7M2x+WXxiSVjYhb5vOaMELiKo3Myr8xgPy8GVl9c0gR97A43TvxhBOBdkfo5G8VMtEWsqm6yaAMvtoOUFAeitCsl/lcYozQmzbJ7352NKAJk8X2YWSNURqTVDYibpnPa8IIias0sqkByM+bkdWDFGEPJbFm0dWsyraQTdVNBmXw1XYAOaX2OSzLWS/zeU8wQrO+koxsdiCSXNa4uGU+rwkjJG4ysr5BirCHklizUM7q61//+he96EU/8zM/87a3vY0/h5BtIZuqmwzK4KvePysq4eeDnFL7HJblrJf5vCcY3qzTP/NTZIpZt/KfOWIjpRwOE6zNcflEkssaF7fM5zVhhMRVGpmVf2MA+XkzsvrmkCLsoSTWLDSz6v+J5MrKyuWXX159HiDbQjZVNxmUwVdXVw8cOMCXauHng5xS+xyW5ayX+bwnGN6s7832uicyxaxb+c8csZHSDIcV1ua4fCLJZY2LW+bzmjBC4iqNzMq/MYD8vBlZfXNIEfZQEmsWmln170dW4LjjjvvBD37gr6x2a2RtAHJK7XNYlrNe5vOeYIQ+fazojGzuEBspzXBMDUSSyxoXt8znNWGExFUa2dQA5OfNyOpBirCHkliz0Mzq+iqOOeaYz3/+8yxHtoVsqm4yDqbryAR/Wux1//I6IBqpdB1ZhodZM/4Hu7sOi/YP5Ed9HdlMjIwvCWQdXkfmD4oGfj7IScKzCL1pl/m8Jxjem3a6/KJDWJvj8ktjkspGxC3zeU0YIXGVZ2RW/o0B5OftjKy+OaQIeyiJNQvNrG7YsOHRRx91D50d+5BtIZuqmwzK4KvtAHJK7XNYlrNe5vOeYIQ+fazojGzuEBspzXBMDUSSyxoXt8znNWGExFUa2dQA5OfNyOpBirCHtwPpDkJ5E9Crr75606ZNp5566nnnnedu+OpDtoVsqm4yKIOvtgPIKbXPYVnOepnPJcYIzTrJ7352NKCRksXenoxsdgDyozay8V8Q6z6iK+HnQ0F5KEKzXuZziTG8Wd+d7fbldz8bg5X/zEETJlrQi5FZm+PyS2OSykbELfN5TRghcZVGZuXfGEB+3oysvjmkCF8dGGRbyKbqeFMGX11d3b9/P1+qhZ8Pckrtc1iWs17mc4kxvFm/KrvKl9/9bAxW/jMHTZhoQS9GZm2Oyy+NSSobEbfM5zVhhMRVGpmVf2MA+XkzsvrmkCJ8dWCQbSGbquNNGXy1HUBOqX0Oy3LWy3wuMUbo0wfJ7352NKAJk8X2YWSNURqTVDYibpnPa8IIias0sqkByM+bkdWDFOGrA4NsC9lUHW/K4KvtAHJK7XNYlrNe5nOJMUKzTvK7nx0NaMJkscnIZgggn4xs6pBtIZuq400ZfPVIv8SVSJdftARNmGhBL0ZmbU66/ILHgI2svjmkCF8dGGRbyKbqeFMGX20HkFNqn8OynPUyn0uMEXrTJvndz44GNGGy2D6MrDFKY5LKRsQt83lNGCFxlUY2NQD5eTOyepAifHVgkG0hm6rjTRl8tR1ATql9Dsty1st8LjFGaNZJfvezowFNmCw2GdkMAeTHaGR01A8Wsi3lur/EQBl81fuzBiX8fJBTap/Dsnstq5Hty/b58rufjcHKf+Yg/UQLejEya3P8v3ExiVvm85owQuIqjczKvzGA/LwZ2RGbw75a/H3ve5//8Ij4lQ/8Cl+qhXX/Rb68GI2eqpsMyuCr+CeWfKkWfj7IKbXPYdm9ltXIdmY7ffndz8Zg5T9zgE7TMjJrc1w+keSyxsUt83lNGCFxlUZm5d8YQH7ejMzaHGu+f+RqYN1/ML+5kbUByCm1z2FZznqZzyXGCH36IPndz44G0zSyxujJyPxiByUukJ83I+sbViPrBMnI5gbJyKjYQYkL5JORVTFcIwvexqdYpA3lbXxoD/3dxod+Q6+/jY/jv3qk29QQf9o+Sm7jswPhFuv5Hzp0aNu2bbTd0218LsguoGKVt/GJ8T/Y3W1waP9Afvec3caHmMdu4yP3f/HFF9fv3/+iTNg/Glmz/bubPtbtX/BvdRufNgA5SXgWoTftMp8kZxF60yb53c+OBnTMy2LTGdkMAeTTGVkVwz0j67yVIKfUPodlOetlPpcYIzTrJL/72dEgGRkVOyhxgXwysipmaWSf+9znfvd3f/fPEU8//bTM8FcI7hxbCT8f5JTa57AsZ73M5xJjeLPuzslJfvezMVj5zxzTNDJrc1x+T0bmxFUamZV/YwD5eTMya3Os+VYjs+4/mL9mZH/1V3/Fn0TEjGzXrl18qRZ+Psgptc9hWc56mc8lxvBmfVu2zZff/WwMVv4zxzSNzNocl9+TkTlxlUZm5d8YQH7ejMzaHGu+1cis+w/mrxnZT/7kT65bt+7Vr351MIMttgTIKbXPYVnOepnPJcYIffog+d3PjgbTNLLG6MnI/GIHJS6Qnzcj6xtWI+sEpZH90z/908c+9rG//du//amf+qmvfvWrMsNfaQ+QU2qfw7Kc9TKfS4wRmnWS3/3saJCMjIodlLhAPhlZFbM0Mn/phBNOeP75593DmJH5v9PVwM8HOaX2OSwvLy/TKy7eBr9PLfllR5717dl2X37vlcOw8p85qA+iBb0YmbU5Lr8USyqL4jqeViNz4iqNzMq/MYD8vBmZtTnWfKuRWfcfzC+Nwl9av37997//ffeweHrjeRsXtiwUseWdWwqWFFs+sratCT8/WxLCUyx5sa/68JatgVjKNi9t3rq0tYizl86mjSKKdUmghs9cROHsRV2uRhdFB4qnZH6bsDbH5RNJLutEXMdz4SMLlXypbETcYmVQ4gL560SlOSwGRYH8mzfzSovYf7Yr1g+/aV2FtTnWfCeuMqz79/MLRyJrKjwKjMxdpVZ8rnzd617nXIyMrPP3hCwTwlMU7z/F+y3GjqVyA7OP/KbN3sf4S84/6ORFFtvHGVljlGdYTFaKFmdkfrGDEhfIz9sZWd9w4k4TZFPZLbfc8sIXvnDDhg1vfvObgxlscTXyfXM18PNBTql9DsuNjexAdsCX33vlMKz8Z45pGpm1OS6/JyNz4iqNzMq/MYD8vBmZtTnWfKuRWfcfzC+NjC97iBmZ/ycgGvj5IKfUPoflxkaW7hDbIazNcfk9GVm6Q2yHsDbHnG80MvP+Q/nNjawNQE6pfQ7LjY2Myc9fcv4xTSNrjJ6MzC92UOIC+Xkzsr5hNbJOkIxsbpCMjIodlLhAPhlZFXNmZO7v4JXw80FOqX0Oy42NjO574eT3XjkMK/+ZY5pGZm2Oy+/JyJy4SiOz8m8MID9vRmZtjjXfamTW/QfzmxuZu+GGEn4+yCm1z2G5sZHtzfb68nuvHIaV/8wxTSOzNsfl92RkTlylkVn5NwaQnzcjszbHmm81Muv+g/nNjawNQE6pfQ7LjY2Myc9fcv4xTSNrjJ6MzC92UOIC+Xkzsr5hNbJO0NzI3L3QlPDzQU6pfQ7LjY3sruwuX37vlcOw8p85pmlk1ua4/J6MzImrNDIr/8YA8vNmZNbmWPOtRmbdfzC/uZEFfwlag3T5RUtM08iszUmXX/AYsJFZm2PONxqZef+h/OZG1gYgp9Q+h+XGRsbk5y85/5imkTVGT0bmFzsocYH8vBlZ37AaWSdIRjY3SEZGxQ5KXCCfjKyKOTMy990BSvj5IKfUPoflxka2O9vty++9chhW/jPHNI3M2hyX35OROXGVRmbl3xhAft6MzNoca77VyKz7D+Y3N7L9+/fzpVr4+SCn1D6H5cZGdlV2lS+/98phWPnPHNM0MmtzXH5PRubEVRqZlX9jAPl5MzJrc6z5ViOz7j+YrzKy4NfBuX9yU34dHG3TxWwg5zni68JyWP6DiXktnBEysvjXwZHw+q+D8//J0MqfFnvdv/w6Lzrmp/N1cKsW/v7XkfX0dXBOX+XXwa1G+B8MfR2Z9evUaIP2D+R3z9nXwdGG/uvajrh//nVtaGTN9q/5Ojja6Ozr4BwhJfx8kJOEZ9HijOz+7H73RKZ407bynznomBct6OWMzNocl18aE5OVosUZmRNXeUZm5d8YQH7ezsiszbHmW8/IrPsP5pNN1U1GzMj8dzwN/HyQU2qfw3JjI0uXX3QIa3Ncfk9Gli6/6BDW5pjzjUZm3n8ov7mRtQHIKbXPYbmxkTH5+UvOP6ZpZI3Rk5H5xQ5KXCA/b0bWN6xG1gmSkc0NkpFRsYMSF8gnI6tizozM/QOeEn4+yCm1z2G5sZHty/b58nuvHIaV/8wxTSOzNsf/11wQi8lK0cLInLhKI7PybwwgP29GZm2ONd9qZNb9B/ObG9mePXv4Ui38fJBTap/DcmMj25nt9OX3XjkMK/+ZY5pGZm2Oy+/JyJy4SiOz8m8MID9vRmZtjjXfamTW/QfzmxtZG4CcUvsclhsbGZOfv+T8Y5pG1hg9GZlf7KDEBfLzZmR9w2pknSAZ2dwgGRkVOyhxgXwysirmzMiCvwStQbr8oiWmaWTW5qTLL3gM2MiszTHnG43MvP9QfnMjawOQU2qfw3JjI2Py85ecf0zTyBqjJyPzix2UuEB+3oysb1iNrBMkI5sbJCOjYgclLpBPRlbFnBmZ+6MnJfx8kFNqn8NyYyNzf6RG8nuvHIaV/8wxTSOzNsfl92RkTlylkVn5NwaQnzcjszbHmm81Muv+g/nNjWzXrl18qRZ+Psgptc9hubGRbcu2+fJ7rxyGlf/MMU0jszbH5fdkZE5cpZFZ+TcGkJ83I7M2x5pvNTLr/oP5zY2sDUBOqX0Oy42NjMnPX3L+MU0ja4yejMwvdlDiAvl5M7K+YTWyTqAysnQbH3kbk773L2/DQsd8uo1PhkbWjP/BI91GxtofIL873cZnnm/j43dHAz8f5CThWbQ4I9uebXdPZIo3bSv/mYOOedGCXs7IrM1x+aUxMVkpWpyROXGVZ2RW/o0B5OftjMzaHGu+9YzMuv9gPtlU3WTEjKwNQE6pfQ7LjY2Myc9fcv4xTSNrjJ6MzC92UOIC+Xkzsr5hNbJOwI3spptuOu+887yEZGRDQTIyKnZQ4gL5ZGRVDMLILrnkEqWRuU+wSvj5IKfUPoflxkZ2IDvgy++9chhW/jPHNI3M2hyX35OROXGVRmbl3xhAft6MzNoca77VyKz7D+ZXjOwf//Ef/+3f/k1pZP4/pmrg54OcUvsclhsbWfoTpQ5hbY7L78nI0p8odQhrc8z5RiMz7z+Uv2Zkt9566ymnnFJsKI2sDUBOqX0Oy42NjMnPX3L+MU0ja4yejMwvdlDiAvl5M7K+YTWyTrBmZOecc86zzz672qmRHTp0iH6cAeSU2uewfFQZWaw/PA9xcGBGFiS/vLwMYjFZKbKseJbSFm+DX5av5fOaMELizpGRuWJ9QP48GxmvZ4JiGFzOLI3sscceK87IHn/88f/4j/8499xziw0/Y+N5Gxe2LBSx5Z1b4AogjLNuOMttx2L9G47JlrJwSO1zWF9cAgsrYmFfubGD8m/ZGoilbPPS5q1LW4s4fel02iiiWJdkWGj49xqX3HnJMW9Yz9uCUTwl84uDv3jK1eii6EDxlMxvE5rmNBB3LfZVH0plI+IWK9mQxAXy14lKc1GgHzdv5pUWsf9sV6wfRf5MxA3mF2PJa5nE+jesd/kLH1mQO6mJxnyKKByJrKnwKDCy73znO38zwaZNmz796U8zq3MPTcgA7hzLDyE8xdF0RgZ9F31ZxQ4EG075sthZnZGhKlLcZVjOQxESF7MN4s7NGdnlgdZg9hyfkcEEBovNoSyXtmOGZ2T+UocfLVG3iKCyF9gOOeul/FxijNCsk/ycyvCQjGySbRA3GdkMMWdGxhAzMvdXBTVA3Zyg36gIKnuB7ZCzXsrPJcbwZt39FQvJz6kIaPj3iiEbmaY5qIoUdxmW81CExMVsg7hKI9Pw7wRAPnhsD9jIrM1x+T0ZWWM+PpobWfCXoAyo29r0VgSVvcB2yFkv5ecSY3izPneXXwzZyDTNQVWkuMuwnIciJC5mG8RVGpmGfycA8sFje8BGZm1O5dqaYLE5lLWWbzSyxnx8NDcyDVC3iKCyF9gOOeul/FxijNCnD5KfUxkehmxkGqAqUtxlWM5DERIXsw3iKo1sagDywWN7wEbWGD0ZWSdIRjYzJCObZBvETUY2Q4zTyNxdOGqAujlBP1gRVPYC2yFnvZSfS4zhzfrubLcvP6cioOHfK4ZsZJrmoCpS3GVYzkMREhezDeIqjUzDvxMA+eCxPWAjszbH5fdkZI35+GhuZBqgbhFBZS+wHXLWS/m5xBihN22Sn1MZHoZsZBqgKlLcZVjOQxESF7MN4iqNbGoA8sFje8BG1hg9GVknSEY2MyQjm2QbxE1GNkOM08jcnR5rgLo5QZ+qCCp7ge2Qs17KzyXG8Gb9/ux+X35ORUDDv1cM2cg0zUFVpLjLsJyHIiQuZhvEVRqZhn8nAPLBY3vARmZtjsvvycga8/HR3MiCvwRlQN3WprciqOwFtkPOeik/lxjDm/V0+UWH0DQHVZHiLsNyHoqQuJhtEFdpZBr+nQDIB4/tARuZtTnp8gsSLiKo7AW2Q856KT+XGCP06YPk51SGhyEbmQaoihR3GZbzUITExWyDuEojmxqAfPDYHrCRNUZPRtYJkpHNDMnIJtkGcZORzRDjNDL3zSg1QN2coHdUBJW9wHbIWS/l5xJjeLO+L9vny8+pCGj494ohG5mmOaiKFHcZlvNQhMTFbIO4SiPT8O8EQD54bA/YyKzN8b8DKVxsDmW5fKuRNebjQ2Vkjb8ODnU7iP+A4v4Wb18p6Dni68KwHUfP18Ht3bs3w+pYd8jI5Nd5kZEN5+vgUBU6Wg95FbwWlvPI18Fl2aeo5KXyH9WWcS8j/Dq4y7O9k4743QGQkc3h18HBBG6eVOrr+3ooi5Ln7+vgNEDdIu9M1AIWoTftUn6SnEXo0wfJz6kMD2RMsjVkZDx7umdkGqAqUly0pjwUIXEx2yCu8oxsagDywZOUAZ+RNQZMYLDYHMpyadYzsk5ANlU3GcnIekIyskm2QdxkZDPEOI3MP3WPAXVbm96KoLIX2A4566X8XGIMb9bT5RcdQtMcVEWKuwzLeShC4mK2QVylkWn4dwIgHzy2B2xk1ua4/J6MrDEfH82NTAPULSKo7AW2Q856KT+XGCP0pk3ycyrDw5CNTANURYq7DMt5KELiYrZBXKWRTQ1APnhsD9jIGqMnI+sEychmhmRkk2yDuMnIZohxGpn79UENUDcnKP3CaiKo7AW2Q856KT+XGMObdffrHpKfUxHQ8O8VQzYyTXNQFSnuMiznoQiJi9kGcZVGpuHfCYB88NgesJFZm+PyezKyxnx8NDcyDVC3iKCyF9gOOeul/FxijNCbNsnPqQwPQzYyDVAVKe4yLOehCImL2QZxlUY2NQD54LE9YCNrjJ6MrBOojCxdRyav02m//3Qd2Wq6jowqTdeRpevIYu9jnMrwQMYkW0NGxrPTGdmk2GxI4gL54ElKOiObLsim6iYjZmS+zceAujlB31IRVPYC2yFnvZSfS4zhzfr2bLsvP6cioOHfK4ZsZJrmoCpS3GVYzkMREhezDeIqjUzDvxMA+eCxPWAjszbH5fdkZI35+GhuZBqgbhFBZS+wHXLWS/m5xBihN22Sn1MZHoZsZBqgKlLcZVjOQxESF7MN4iqNbGoA8sFje8BG1hg9GVknSEY2MyQjm2QbxE1GNkOM08jcP8XVAHVzgn6hIqjsBbZDznopP5cYw5v1A9kBX35ORUDDv1cM2cg0zUFVpLjLsJyHIiQuZhvEVRqZhn8nAPLBY3vARmZtjsvvycga8/HR3MgOHz7MlwRQNyfo4YqgshfYDjnrpfxcYgxv1h/IHvDl51QENPx7xZCNTNMcVEWKuwzLeShC4mK2QVylkWn4dwIgHzy2B2xk1ua4/J6MrDEfH82NTAPULSKo7AW2Q856KT+XGCP06YPk51SGhyEbmQaoihR3GZbzUITExWyDuEojmxqAfPDYHrCRNUZPRtYJkpHNDMnIJtkGcZORzRDjNDJ36V0NUDcnKF0KOxFU9gLbIWe9lJ9LjOHNOl0K6+TnVAQ0/HvFkI1M0xxURYq7DMt5KELiYrZBXKWRafh3AiAfPLYHbGTW5rj8noysMR8fpZF97WtfO/PMM0888cTFxcVgBltUAnWLCCp7ge2Qs17KzyXGCL1pk/ycyvAwZCPTAFWR4i7Dch6KkLiYbRBXaWRTA5APHtsDNrLG6MnIOkFpZH//93///ve//4477njVq171Z3/2ZzLDX9EDdYsIKnuB7ZCzXsrPJcYIzTrJz6kMD8nIJtkGcZORzRBzYGT+0mmnneY/jBmZ+/OoGqBuTlD3B2e4LnuB7ZCzXsrPJcbwZt39OR7Jz6kIaPj3iiEbmaY5qIoUdxmW81CExMVsg7hKI9Pw7wRAPnhsD9jIrM1x+T0ZWWM+PtaM7Ld/+7fXrVt3zDHHPPPMMzLDXyEcOnSILwmgbk7QQxVBZS+wHXLWS/m5xBjerN+X3efLz6kIaPj3iiEbmaY5qIoUdxmW81CExMVsg7hKI9Pw7wRAPnhsD9jIrM1x+T0ZWWM+PtaM7JFHHvnsZz+7Y8eOJ598Umb4K3qgbhFBZS+wHXLWS/m5xBihTx8kP6cyPAzZyDRAVaS4y7CchyIkLmYbxFUa2dQA5IPH9oCNrDF6MrJOsGZkDuvXr3/00Ufdw+LpjedtXNiyUMSWd24pWOojW8qypcVsaYcI0QiKpWxxCaa8iIV95cYO2EmW3bI1EEvZ5qXNW5e2sijWJZlZxSV3XoJ9CIer0UXRgcXbFuV+isUiXxZbdCCY33dExH25SdyXG8UtVgYlLpC/TlRaxP9dK9YPyL95M6+0iP1ny2K34iTPRNxgwAQGi0Vx12IfH3IZ6994jNx/gygciayp8KiAkX35y192D2NnZO52QjXIAO6d6YOVdybZi7ySvcN4RrY72+2/j3EqAhr+nQD6ezm+b7N4NZTlanQxhDMyTXNQFSnuMiznoQiJi9kGcZVnZBr+nQDIB09SBnxGZm2Oy68/I4O5xSgcnDZuKlavvx7qleGJ2JiPj/KM7HWve92NN954xx13/NzP/dyf/MmfyAx/RQ/ULSKo7MWkHZRhNTImP6cyO0TlvxzKkq0ZgpFpgKpIcZdhWRabV7KtRuYXmw1JXCAfEVe2BrNnb2SNEZ3kHMpyNVbEDRa7AnXxvbdDaWR/8Rd/cdppp23YsOHSSy8NZrBFJVC3iKCyF9gOOeu0F96ISTti8nMqs0NU/mRkychcJCNrh9LI+LKHmJG5W9bWAHVzgj5VEVT2AtshZ532whsxaYeT//7sfvdEpmiThn8niMo/YCPTNAdVkeLC9PJKKULiYrZBXKWRafh3AiAfEXewRmZtjsuPTnIOZbkarUbWmI+P5kYWXGRA3ZygvrKiEZN2yFmnvfBGTNrh5PfnIPPaFIOGfyeIyj9gI9PsEFWR4sL08kopQuJitkFcpZFp+HcCIB8Rd7BGZt2hy49Ocg5luRqtRtaYD1sEenzZA2XwVR1Qt4igshfYDjnrtBfeiEk7YvJzKrNDVP4BG5kGqIoUF6aXV0oREhezDeIqjWxqAPIRcWVrMDtybE/RyBojOsk5lOVqtBpZJ0hG1jui8icjS0bmIhlZO6iMLPh1cOeffz5tqL8O7g6srq+vg9uX7VuxfB2c478a+bqz+q9TO+L+3deRQX8XJwWeM/m6sCJ+AcoC4Yf3dXBFQ4Jfpxb/OribJhX08nVwV2dXU7HKr4OL8T94pK8jU/ZndaIvkN89Z18HR3vTf13bhz70IdXXwWF8amJkD/lG5vQtHpK+WSb3v6r7OjjJP30d3DQA/Q2+j6UzsnRG5iKdkbUD2VTdTpORtURU/mRkychcJCNrh2RkvSMqfzKyZGQukpG1Q3Mj8z+jxoC6OUEfqggqe4HtkLNOe+GNmLTDyU//pkCRKdqk4d8JovIP2Mg0zUFVpLgwvbxSipC4mG0QV2lkGv6dAMhHxB2skVmb4/Kjk5xDWa5Gq5E15uOjuZFpgLpFBJW9wHbIWae98EZM2hGTn1OZHaLyD9jINEBVpLgwvbxSipC4mG0QV2lkUwOQj4grW4PZkWN7ikbWGNFJzqEsV6PVyDpBMrLeEZU/GVkyMhfJyNqhuZG530PXAHVzgtJv3ieCyl5gO+Ss0154IybtcPK731uv6IxMw78TROUfsJFpmoOqSHFhenmlFCFxMdsgrtLINPw7AZCPiDtYI7M2x+VHJzmHslyNViNrzMdHcyPTAHWLCCp7ge2Qs0574Y2YtCMmP6cyO0TlH7CRaYCqSHFhenmlFCFxMdsgrtLIpgYgHxFXtgazI8f2FI2sMaKTnENZrkarkXWCZGS9Iyp/MrJkZC6SkbVDMrLeEZU/GVkyMhfJyNqhuZH5f/cQA+rmBH1LRVDZi7ySbTWy7dl290SmaJOGfyeIyj9gI9M0B1WR4sL08kopQuJitkFcpZFp+HcCIB8Rd7BGZm2Oy49Ocg5luRqtRtaYj4/mRqYB6hYRVPYC2yFnnfbCGzFpR0x+TmV2iMo/YCPTAFWR4sL08kopQuJitkFcpZFNDUA+Iq5sDWZHju0pGlljRCc5h7JcjVYj6wTJyHpHVP5kZMnIXCQja4fmRub+Nr0GqJsT9AsVQWUvsB1y1mkvvBGTdjj5D2QH3BOZok0a/p0gKv+AjUzTHFRFigvTyyulCImL2QZxlUam4d8JgHxE3MEambU5Lj86yTmU5Wq0GlljPj5URha8jc9rX/ta2lDfxucwVtfXbXweyB5YsdzGx/Ffjdympv42OEfc/1zfxqd4NngbnPhtfP51UkEvt/H5aPZRKlZ5G58Y/4Oh29RYb4NDG/N7G5/iqVXLbXwefvjhXm/j4/a/qruNj+SfbuMzDUB/g+9jAz4j0wBVkeLC9PJKKULiYrZBXOUZ2dQA5CPiytZgduQkZYpnZI0RneQcynI1Ws/IOgHZVN1Ok5G1RFT+ZGTJyFwkI2uH5kbmTmJrgLo5QelD5URQ2Qtsh5x12gtvxKQdTn76UEmRKdqk4d8JovIP2Mg0zUFVpLgwvbxSipC4mG0QV2lkGv6dAMhHxB2skVmb4/Kjk5xDWa5Gq5E15uOjuZFpgLpFBJW9wHbIWae98EZM2hGTn1OZHaLyD9jINEBVpLgwvbxSipC4mG0QV2lkUwOQj4grW4PZkWN7ikbWGNFJzqEsV6PVyDpBMrLeEZU/GVkyMhfJyNqhuZG5XzTUAHVzgrpf3eC67AW2Q8467YU3YtIOJ/9d2V3uiUzRJg3/ThCVf8BGpmkOqiLFhenllVKExMVsg7hKI9Pw7wRAPiLuYI3M2hyXH53kHMpyNVqNrDEfH82N7NChQ3xJAHVzgh6qCCp7ge2Qs0574Y2YtMPJf192n3si89oUg4Z/J4jKP2Aj0zQHVZHiwvTySilC4mK2QVylkWn4dwIgHxF3sEZmbY7Lj05yDmW5Gq1G1piPD5WRBa8jc9fpqK8jo+r6uo6MOqS/jix4nZH+Oiz9/qG/83Yd2aqiP6gKHa3+lVK9XEfm9FVeR7Ya4X8wdJ2U9Tos2pjf68hoQ38dmds/TGAP15H5/DXXkdFGuo5s2oD+Bt/HBnxGpgGqIsWF6eWVUoTExWyDuMozsqkByEfEla3B7MhJyhTPyBojOsk5lOVqtJ6RdQKyqbqdxozMGWoNUDcn6AcrgspeYDvkrNNeeCMm7XDy7852uycyRZs0/DtBVP4BG5mmOaiKFBeml1dKERIXsw3iKo1Mw78TAPmIuIM1MmtzXH50knMoy9VoNbLGfHyURnbFFVdcc801d95554te9KKvfe1rMsNf0QN1iwgqe4HtkLNOe+GNmLQjJj+nMjtE5R+wkWmAqkhxYXp5pRQhcTHbIK7SyKYGIB8RV7YGsyPH9hSNrDGik5xDWa5Gq5F1gtLI/KVXvOIV/sNkZC0RlT8ZWTIyF8nI2iFgZNu3b/cfxozM/aNgDVA3J+hTFUFlL7AdctZpL7wRk3Y4+e/P7ndPZIo2afh3gqj8AzYyTXNQFSkuTC+vlCIkLmYbxFUamYZ/JwDyEXEHa2TW5rj86CTnUJar0Wpkjfn44Eb2ghe84Pnnn/cSokYWXGRA3ZygvrKiEZN2yFmnvfBGTNrh5PfnIPPaFIOGfyeIyj9gI9PsEFWR4sL08kopQuJitkFcpZFp+HcCIB8Rd7BGZt2hy49Ocg5luRqtRtaYD1sEevTgySef3LRpUzUhamQaoG4RQWUvsB1y1mkvvBGTdsTk51SmgkOHDlG7fCwvL4fljxtZ8SN8L7SfaRmZBqiKFBdI8kopQuJitkFcpZH1Aa4HAshHxJWtoZaFj+0pGpkGtknOoSxXo9LI+N4RwWvENKAfh8lYXFw8+eST+fPJyNSAPpYVsLgpLH/EyED+66+HCWDx1rdCG0SxycimABR3WSiLikfEla2hloWP7YEZGRKVxUYmOYdsV6PSyMR83349XJzWUNzSyJ577rkNGzY8+OCD/Pm4kbmL6GowaQfVdUdFUNmLvJJtNbJ92T73RKZoh4a/CRMjc6xdRN7HaowsKP973wtt4Ku9GJmmOVisFBfo80opQuJitkFcpZFp+JuA4kasKSJuJDsq7tSMTNMcJOpYe+IGi80r2Uojcw86Ebc0sm3btq33IDP8FT2wHRFBZS/ySrbVyPzIFO3oHGMyMg2wWCku0OeVUoTExWyDuMpZ7xxjMjINkKikH5nkvJJtNTIXbcQtjYwve0hGpkQyMkefV0oREhezDeK2mfU2SEaGEZnkvJKdjKySnYyMRzKydrPeBsnIMCKTnFey58zI/D/ajAHb4QR9qCKo7EVeybYaGf2RLUWmaIeGvwljMjJNc7BYKS7Q55VShMTFbIO4ylnX8DdhTEamaQ4Sdaw9cYPF5pVsq5F1Im5zI9MA2xERVPYir2RbjcyPTNGOzjEmI9MAi5XiAn1eKUVIXMw2iKuc9c4xJiPTAIlK+pFJzivZViNz0UZclZGl2/jI26TI/U+MjG5UA4KuyW+5jU8pP7vNy0ppZOk2PsX6alP+B2tvU7Ma749nZEzfcd7GB4m6GwG4CpY7vI2PuxGA09c3sundxsftsQbYDvfO5CYA16kFLEJv2rSXshEsvDdtNwEkP6cioOFvwsTIHGsXkfexAZ+RaZqDxUpxgT6vlCIkLmYbxFW+aWv4m+AZGYv5OyPTNAeJOtaeuMFi80q29YysE3HJpup+OGZkGmA7IoLKXuSVbKuR+ZEp2tE5xmRkGmCxUlygzyulCImL2QZxlbPeOcZkZBogUUk/Msl5JdtqZC7aiJuMrDMkI3P0eaUUIXEx2yBum1lvg2RkGJFJzivZycgq2cnIeCQjazfrbZCMDCMyyXkle86MzP8XuBiwHU7QeyqCyl7klWyrkd2Q3eCeyBTt0PA3YUxGpmkOFivFBfq8UoqQuJhtEFc56xr+JozJyDTNQaKOtSdusNi8km01sk7EbW5kGmA7IoLKXuSVbKuR+ZEp2tE5xmRkGmCxUlygzyulCImL2QZxlbPeOcZkZBogUUk/Msl5JdtqZC7aiJuMrDMkI3P0eaUUIXEx2yBum1lvg2RkGJFJzivZwzWy4HVkF110EW2oryP7AlbX13VkB7IDK5bryBz/1ch1UvXXYcn9T4xsDNeRFU8Fr8OKX0e2PKmgl+vI3pu9l4pVXkcW43+w6XVYnpHN/XVktG65juyTvV5Hlme56Toyyb/VdWTFK/ElAWyHe2c6PNnAdWoBi9CbNu2lbAQL7037gewB90Q2aUcNNPxNmBiZY+0i8j424DMyTXOwWCku0OeVUoTExWyDuMo3bQ1/EzwjYzF/Z2Sa5iBRx9oTN1hsXsm2npF1Ii7ZVN0Px4xMA2xHRFDZi7ySbTUyPzJFOzrHmIxMAyxWigv0eaUUIXEx2yCuctY7x5iMTAMkKulHJjmvZFuNzEUbcZORdYZkZI4+r5QiJC5mG8RtM+ttkIwMIzLJeSV7zozMfbl5DbAdTtADFUFlL/JKttXI9mZ73ROZoh0a/iaMycg0zcFipbhAn1dKERIXsw3iKmddw9+EMRmZpjlI1LH2xA0Wm1eyrUbWibjNjUwDbEdEUNmLvJJtNTI/MkU7OseYjEwDLFaKC/R5pRQhcTHbIK5y1jvHmIxMAyQq6UcmOa9kW43MRRtxk5F1hmRkjj6vlCIkLmYbxG0z622QjAwjMsl5JXvOjMz9xrcG2A4nqPsdNK7LXuSVbKuRuTu9rOiMTMPfhDEZmaY5WKwUF+jzSilC4mK2QVzlrGv4mzAmI9M0B4k61p64wWLzSrbVyDoRt7mRab6BDtvhBD1UEVT2Iq9kW43svuw+90SmaIeGvwljMjJNc7BYKS7Q55VShMTFbIO4ylnX8DdhTEamaQ4Sdaw9cYPF5pVsq5F1Im5zI9MA2xERVPYir2RbjcyPTNGOzjEmI9MAi5XiAn1eKUVIXMw2iKuc9c4xJiPTAIlK+pFJzivZViNz0UbcZGSdIRmZo88rpQiJi9kGcdvMehskI8OITHJeyZ4zI9u/fz9fEsB2OEH3VwSVvcgr2VYjuyq7yj2RKdqh4W/CmIxM0xwsVooL9HmlFCFxMdsgrnLWNfxNGJORaZqDRB1rT9xgsXkl22pknYjb3Mg0wHZEBJW9yCvZViPzI1O0o3OMycg0wGKluECfV0oREhezDeIqZ71zjMnINECikn5kkvNKttXIXLQRNxlZZ0hG5ujzSilC4mK2Qdw2s94GycgwIpOcV7LnzMjcX+HXANvhBH2qIqjsRV7JthrZ/dn97olM0Q4NfxPGZGSa5mCxUlygzyulCImL2QZxlbOu4W/CmIxM0xwk6lh74gaLzSvZViPrRFyVkQVv47O4uEgb6tv4kLJ93caH5kB/Gx/HfzVym5r62+DI/U+MbAy38SlqCd4GJ34bn09OKujlNj43ZjdSscrb+MT4H2x6GxzPyOb+Nj7kjJbb+Pxdr7fxuTm72XQbH8m/1W18NMB2RN6ZqAUsQm/atJeyESxCnz5Ifk6lf0yMTBYbeR8b8BmZBlisFBfo80opQuJitkFc5Zt25/CMjMX8nZFpgEQl/cgk55Vs6xmZizbikk3V/XAyMiWSkTn6vFKKkLiYbRC3zay3QTIyjMgk55XsGRvZunXrNm3atH79+mAGW1zFT5R8SQDb4QTdUxFU9iKvZFuNbGe20z2RKdqh4W/CmIxM0xwsVooL9HmlFCFxMdsgrnLWNfxNGJORaZqDRB1rT9xgsXkl22pknYi7ZmRPPvnkKtpZMIMtKoHtiAgqe5FXsq1G5kemaEfnGJORaYDFSnGBPq+UIiQuZhvEVc565xiTkWmARCX9yCTnlWyrkbloI+6akRGSkTVGMjJHn1dKERIXsw3itpn1NkhGhhGZ5LySnYyskp2MjEcysnaz3gbJyDAik5xXsufMyPxff8aA7XCCPlQRVPYir2RbjYx+XU2RKdqh4W/CmIxM0xwsVooL9HmlFCFxMdsgrnLWNfxNGJORaZqDRB1rT9xgsXkl22pknYirMrKN521c2LJQxJZ3btlxzw59ZEtZtrSYLe0QIRpBsZQtLkEjiljYV27sgJ1k2S1bA7GUbV7avHVpK4tiXZLpOxZvW8R6ZbEvz64TlRbxf6EuV6OLlxc7uXkzr7SI/WcX+bLYogPFS0s+fUdE3JebxIViLeIWK7MTVxaLTYiI64r1A/Ij4spit+Ikz05cWWxkklFcV2NF3GCxKK4stoG4hSORNRUedWQja/yekAEi70yyF3kle4fxjMyPTOHrnWNMZ2QaYLFSXKDPK6UIiYvZBnGVb9qdY0xnZBogUUk/Msl5JbsibrDYFahLLLUSd+2MjK69cGAZaz8xwa5du/iSALbDCbqrIqjsRV7JthrZtmybeyJTtEPD34QxGZmmOVisFBfo80opQuJitkFc5axr+JswJiPTNAeJOtaeuMFi80q21cg6EXfNyGKIGZkG2I6IoLIXeSXbamR+ZIp2dI4xGZkGWKwUF+jzSilC4mK2QVzlrHeOMRmZBkhU0o9Mcl7JthqZizbiJiPrDMnIHH1eKUVIXMw2iNtm1tsgGRlGZJLzSnYyskp2MjIeycjazXobJCPDiExyXsmeMyPz/yQ9BmyHE/SeiqCyF3kl22pkN2Q3uCcyRTs0/E0Yk5FpmoPFSnGBPq+UIiQuZhvEVc66hr8JYzIyTXOQqGPtiRssNq9kW42sE3GbG5kG2I6IoLIXeSXbamR+ZIp2dI4xGZkGWKwUF+jzSilC4mK2QVzlrHeOMRmZBkhU0o9Mcl7JthqZizbiJiPrDMnIHH1eKUVIXMw2iNtm1tsgGRlGZJLzSvacGZl/47oYsB1r01sRVPYir2YbjczdaHBFZ2Qa/iaMycg0zcFipbhAn1dKERIXsw3iKmddw9+EMRmZpjlI1LH2xA0Wm1ezjUbWibjNjezw4cN8SQDb4QQ9XBFU9iKvZFuN7IHsAfdEpmiHhr8JYzIyTXOwWCku0OeVUoTExWyDuMpZ1/A3YUxGpmkOEnWsPXGDxeaVbKuRdSJucyPTANsREVT2Iq9kW43Mj0zRjs4xJiPTAIuV4gJ9XilFSFzMNoirnPXOMSYj0wCJSvqRSc4r2VYjc9FG3GRknSEZmaPPK6UIiYvZBnHbzHobJCPDiExyXsmeMyM7cOAAXxLAdjhBD1QElb3IK9lWI9ub7XVPZIp2aPibMCYj0zQHi5XiAn1eKUVIXMw2iKucdQ1/E8ZkZJrmIFHH2hM3WGxeybYaWSfiNjcyDbAdEUFlL/JKttXI/MgU7egcYzIyDbBYKS7Q55VShMTFbIO4ylnvHGMyMg2QqKQfmeS8km01MhdtxFUZWfDr4NzvDtRfB0fV9fV1cNQL/dfBBb8ujPF3i/LrtuT+J0Y2hq+DW1X0B4ulo9X/wrNevg7O6av8OrjVCP+DTb9OzTOyuf86ONqwfB2cq6CXr4Nz+vpGVvN1cLTR2dfBBX8JyoDtWHsbnmzgOrWARehNm/ZSNoKF96adLr/oEJrmYLFSXKDPK6UIiYvZBnGVb9oa/iZ4RsZi/s7INM1Boo61J26w2LyabTwj60Rcsqm6H44ZWfE+wJcEsB1O0EMVQWUv8kq21cgKX3dPZIp2aPibMCYj0zQHi5XiAn1eKUVIXMw2iKucdQ1/E8ZkZJrmIFHH2hM3WGxeybYaWSfiNjcyDbAdEUFlL/JKttXI/MgU7egcYzIyDbBYKS7Q55VShMTFbIO4ylnvHGMyMg2QqKQfmeS8km01MhdtxE1G1hmSkTn6vFKKkLiYbRC3zay3QTIyjMgk55XsOTOy/fv38yUBbIcTdH9FUNmLvJJtNbKrsqvcE5miHRr+JozJyDTNwWKluECfV0oREhezDeIqZ13D34QxGZmmOUjUsfbEDRabV7KtRtaJuM2NTANsR0RQ2Yu8km01Mj8yRTs6x5iMTAMsVooL9HmlFCFxMdsgrnLWO8eYjEwDJCrpRyY5r2RbjcxFG3GTkXWGZGSOPq+UIiQuZhvEbTPrbZCMDCMyyXkle86MLPhLUAZsx9r0VgSVvcir2UYjS5dfdAhNc7BYKS7Q55VShMTFbIO4ylnX8DdhTEamaQ4Sdaw9cYPF5tVso5F1Im5zIwsuMmA7nKC+sqIRFKFZp73wRkza4eT35yBTtEPD34QxGZlmh1isFBfo80opQuJitkFc5axr+JswJiPT7BCJOtaeuMFi80q21cg6EZdsqu6HKYOv6oDtiAgqe5FXsq1G5kemaEfnGJORaYDFSnGBPq+UIiQuZhvEVc565xiTkWmARCX9yCTnlWyrkbloI24yss6QjMzR55VShMTFbIO4bWa9DZKRYUQmOa9kz5mR7dmzhy8JYDucoHsqgspe5JVsq5HtzHa6JzJFOzT8TRiTkWmag8VKcYE+r5QiJC5mG8RVzrqGvwljMjJNc5CoY+2JGyw2r2RbjawTcZsbmQbYjoigshd5JdtqZH5kinZ0jjEZmQZYrBQX6PNKKULiYrZBXOWsd44xGZkGSFTSj0xyXsm2GpmLNuImI+sMycgcfV4pRUhczDaI22bW2yAZGUZkkvNK9nCNLHgbn2KRNtS38dmB1fV1Gx/6Ja7+Nj6O/2rkNjX1t8GR+58Y2Rhu47MD4RaD/cFi6Wg9lGXbJhX0chufC7ILqFjlbXxi/A82vQ2OZ2Rzfxsf6ozlNj4X93obn1/MftF0Gx/Jv9VtfPwdxYDtcO9MD002cJ1awCL0pk17KRvBwnvTJuEpskk7aqDhb8LEyBxrF5H3sQGfkWmag8VKcYE+r5QiJC5mG8RVvmlr+JvgGRmL+Tsj0zQHiTrWnrjBYvNKtvWMrBNxyabqfjhmZBpgOyKCyl7klWyrkfmRKdrROcZkZBpgsVJcoM8rpQiJi9kGcZWz3jnGZGQaIFFJPzLJeSXbamQu2oi7ZmTXXnvtGWec8cu//MvBDLaoBLYjIqjsRV7JTkbGIxlZu1lvg2RkGJFJzivZszSyL33pS3/0R39UPP7Rj3500UUXyQx/hbBr1y6+JIDtcILuqggqe5FXsrdc6Gcfeda3ZdvcE5miHRr+JozJyDTNwWKluECfV0oREhezDeIqZ13D34QxGZmmOUjUsfbEDRabV7Ir4gaLXYG63INOxC2N7Pd///e///3v09L69eu/9a1vsQz30ARsR0RQ2Yu8kh3+x37Rjpj8nEr/GJORaYDFSnGBPq+UIiQuZhvEVc565xiTkWmARCX9yCTnleyKuMFiV6AusdRK3NLIXvayl7mldevWffSjH2UZ7qGD/6uEGLAdTtB7KoLKXuSVbKuR3ZDd4J7IFO3Q8DdhTEamaQ4WK8UF+rxSipC4mG0QVznrGv4mjMnINM1Boo61J26w2LySbTWyTsQtjeyss85yS4WR/emf/inLcA8d/F9vx4DtcILuqAgqe5FXsq1Glu5+0SE0zcFipbhAn1dKERIXsw3iKmddw9+EMRmZpjlI1LH2xA0Wm1eyrUbWibilkb3mNa9xS4WR/d3f/Z17uLxcDltCQkLCYAFO9aUvfekP//APC9v68Y9/vHXrVudiCQkJCfMCOJ3bsGHDtddeW7jYF7/4Rf58QkJCwuBx5M+lCQkJCQNHMrKEhIS5RzKy2WP9+vWf/vSn+eoY8c1vfvPAgQNPPPEEf2Jc+OEPf0gb3/3udx966KHR1zsEDMXI3vSmN73iFa/4+Mc//vzzz9PK8vJycYRXs0aC86pYt27dpk2bNm/ezPNGgVtuuYU2fvM3f7MQtCh2w4YNN9xwQzVrJCgs7Nd//dePPfbY3/u937v11ltPOumkouTi4XPPPcdTR4f//u///t///V++Oi0Mwsh27dr12GOPFRt33333C17wgocffnh11EZ28sknX3LJJe5hcWz/zd/8jff8qFAczMX/i/ena665xi3+xm/8xlrGiHDuuee+9a1vLTbuu+++3/qt3/LX15LGhZe//OUvfelLixOR/fv3X3vttcV2Mc//9V//xfN6xiCMjGbd4YILLigO9REbGeH888//4z/+42effXbcRuYuYvyd3/kdt3jllVe67THhxS9+8Yc+9KFi46tf/eqdd97p1k8//fS1pHHh5ptv5kurqxs3buRLPWMQRvYLv/AL/sPiHHVxcXHnzp3jNrLi48app556zjnnFGWO2MgOHjx4xRVXPPLII8Xb1Tve8Y5HH330jW9841iVLQz6JS95ydNPP11M72WXXfbtb3+7WCw+bfzar/0aTx0Lik/QfAk/c/ClnjEII/vyl7/8z//8z2yx+CSybds2tjhKfO5zn/vOd77DV0eE733ve7fddltxBnrWWWddeumlX/nKV3jGiPCf//mf11133YMPPlhs33vvvcVHreAf1owGL3zhCwv7/shHPvKJT3yi+BRVbBfvWF//+td5Xs8YhJElJCTMKb71rW8tLCysm+Cnf/qn3/72t/Ok/pGMLCEhoWMcOnSIL/WMZGQJCQkdY/r/BpqMLCEhoTnuCiEZWUJCwjzhV3/1V/+fQDKyhISEecKmTZv4UvpomZCQMF94/PHH+dIs8P8B7w44ZTyIO84AAAAASUVORK5CYII=>