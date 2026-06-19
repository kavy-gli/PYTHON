import math
from utils import *

def main_menu():
    while True:
        print("\n=== Multi-Utility Toolkit ===")
        print("1. Datetime Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module (dir)")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current Date & Time:", current_datetime())

        elif choice == "2":
            num = int(input("Enter number for factorial: "))
            print("Factorial:", factorial(num))

        elif choice == "3":
            length = int(input("Enter password length: "))
            print("Random Password:", random_password(length))

        elif choice == "4":
            print("UUID1:", generate_uuid1())
            print("UUID4:", generate_uuid4())

        elif choice == "5":
            filename = input("Enter filename: ")
            create_file(filename)
            data = input("Enter data to write: ")
            print(write_file(filename, data))
            print("File Content:", read_file(filename))

        elif choice == "6":
            module_name = input("Enter module name (example: math): ")
            mod = __import__(module_name)
            print(explore_module(mod))

        elif choice == "7":
            print("Thank you for using Toolkit!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()