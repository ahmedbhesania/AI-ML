class Employee:
    def __init__(self, name, age, employee_id=None, salary=None):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.salary = salary

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Salary: {self.salary}")

    def __del__(self):
        print(f"Employee {self.name} is being deleted.")
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")
class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
def main_menu():
    while True:
        print("Employee Management System , created by ahmed:")
        print("Choose an operation:")
        print("1. Create an Employee")
        print("2. Create a Manager")
        print("3. Create a Developer")
        print("4. Show Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            emp = Employee(name, age, employee_id, salary)
            print(f"Employee created with name: {name}, age: {age}, ID: {employee_id}, and salary: {salary}.")

        elif choice == '2':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            mgr = Manager(name, age, employee_id, salary, department)
            print(f"Manager created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and department: {department}.")

        elif choice == '3':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            programming_language = input("Enter Programming Language: ")
            dev = Developer(name, age, employee_id, salary, programming_language)
            print(f"Developer created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and programming language: {programming_language}.")

        elif choice == '4':
            detail_choice = input("Choose details to show:\n1. Employee\n2. Manager\n3. Developer\nEnter your choice: ")
            if detail_choice == '1':
                Employee.display()
            elif detail_choice == '2':
                Manager.display()
            elif detail_choice == '3':
                Developer.display()
            else:
                print("Invalid choice!")

        elif choice == '5':
            print("Exiting the system. All resources have been freed.\nGoodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main_menu()










    
