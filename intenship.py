class Employee:
    def __init__(self, emp_id, name, basic_salary, attendance):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.attendance = attendance

    def calculate_salary(self):
        working_days = 30


        salary = (self.basic_salary / working_days) * self.attendance

        
        bonus = 0
        if self.attendance >= 28:
            bonus = self.basic_salary * 0.10

        # Total Salary
        total_salary = salary + bonus

        return salary, bonus, total_salary

    def generate_payroll(self):
        salary, bonus, total_salary = self.calculate_salary()

        print("\n========== PAYROLL REPORT ==========")
        print(f"Employee ID   : {self.emp_id}")
        print(f"Employee Name : {self.name}")
        print(f"Basic Salary  : ₹{self.basic_salary:.2f}")
        print(f"Attendance    : {self.attendance} days")
        print(f"Salary Earned : ₹{salary:.2f}")
        print(f"Bonus         : ₹{bonus:.2f}")
        print(f"Net Salary    : ₹{total_salary:.2f}")
        print("====================================")


emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
attendance = int(input("Enter Attendance (Days Present): "))

employee = Employee(emp_id, name, basic_salary, attendance)
employee.generate_payroll()