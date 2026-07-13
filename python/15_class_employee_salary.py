# Q15 Employee gross salary - @JIYO P V 2026-07-13
class Employee:
    def __init__(self, emp_id, name, basic_pay):
        self.emp_id = emp_id
        self.name = name
        self.basic_pay = basic_pay

    def calculate_salary(self):
        hra = 0.20 * self.basic_pay
        da = 0.10 * self.basic_pay
        return self.basic_pay + hra + da


e = Employee(1, "Ravi", 30000)
print("Employee ID:", e.emp_id)
print("Name:", e.name)
print("Basic Pay:", e.basic_pay)
print("Gross Salary:", e.calculate_salary())
