class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        print("Person resources freed.")


class Employee(Person):

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)

    def __del__(self):
        print("Employee resources freed.")


class Manager(Employee):

    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_emp_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)

    def __del__(self):
        print("Manager resources freed.")


person = None
employee = None
manager = None

while True:

    print("\n--- Python OOP Project: Employee Management System ---")
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Check Inheritance")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        print(f"\nPerson created with name: {name} and age: {age}.")

    elif choice == 2:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)

        print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")

    elif choice == 3:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)

        print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {department}.")

    elif choice == 4:

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        detail_choice = int(input("Enter choice: "))

        if detail_choice == 1:
            if person:
                person.display()
            else:
                print("No Person created.")

        elif detail_choice == 2:
            if employee:
                employee.display()
            else:
                print("No Employee created.")

        elif detail_choice == 3:
            if manager:
                manager.display()
            else:
                print("No Manager created.")

        else:
            print("Invalid choice.")

    elif choice == 5:

        print("\nInheritance Check:")
        print("Employee is subclass of Person:",
              issubclass(Employee, Person))

        print("Manager is subclass of Employee:",
              issubclass(Manager, Employee))

    elif choice == 6:

        print("\nExiting the system. All resources have been freed.")
        del person
        del employee
        del manager

        print("\nGoodbye!")
        break

    else:
        print("Invalid Choice!")

    print("\n--- Choose another operation ---")
