print("Welcome To Student Data Organizer")

print("Select an option to continue:")

    print("1.Add Student")
    print("2.Display student")
    print("3.Update student data ")
    print("4. Delete student ")
    print("5. Display student subject")
    print("6. Exit")
choice=int(input("Enter your choice: "))

student = []

students = {    
    "st1": {"ID": "ST101", "Name": "Aarav Patel", "Age": 17, "Grade": "A+", "Date of birth dd/mm/yyyy": "15-03-2009"},
    "st2": {"ID": "ST102", "Name": "Diya Shah", "Age": 16, "Grade": "A", "Date of birth dd/mm/yyyy": "22-07-2010"},
    "st3": {"ID": "ST103", "Name": "Krish Mehta", "Age": 17, "Grade": "B+", "Date of birth dd/mm/yyyy": "09-11-2009"},
    "st4": {"ID": "ST104", "Name": "Riya Desai", "Age": 16, "Grade": "A", "Date of birth dd/mm/yyyy": "30-01-2010"},
    "st5": {"ID": "ST105", "Name": "Vivaan Joshi", "Age": 17, "Grade": "A+", "Date of birth dd/mm/yyyy": "18-05-2009"}
}

match choice:
    case 1:
        print("you have selected option 1")
        print("Enter your student details:")
        id=input("Enter your id: ")
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        grade=input("Enter your grade: ")
        date=input("Enter your date of birth dd/mm/yyyy:")
        subject=input("Enter your subject: ")
        print("Student details added successfully!")
        print("Here is your quick check:")
        print("=========================")
        print("ID:",id)
        print("---------------------------")
        print("Name:",name)
        print("---------------------------")
        print("Age:",age)
        print("---------------------------")
        print("Grade:",grade)
        print("---------------------------")
        print("Date of Birth:",date)
        print("---------------------------")
        print("Subject:",subject)
        print("=========================")
        student.append({"ID":id,"Name":name,"Age":age,"Grade":grade,"Date of birth dd/mm/yyyy":date,"Subject":subject})
    case 2:
        print("you have selected option 2")
        print("Here is the student data:")
        for key, info in students.items():
            print("=========================")
            print("ID:", info["ID"])
            print("---------------------------")
            print("Name:", info["Name"])
            print("---------------------------")
            print("Age:", info["Age"])
            print("---------------------------")
            print("Grade:", info["Grade"])
            print("---------------------------")
            print("Date of Birth:", info["Date of birth dd/mm/yyyy"])
            print("=========================")
        if student:
            print("Added students at runtime:")
            for info in student:
                print("=========================")
                print("ID:", info["ID"])
                print("---------------------------")
                print("Name:", info["Name"])
                print("---------------------------")
                print("Age:", info["Age"])
                print("---------------------------")
                print("Grade:", info["Grade"])
                print("---------------------------")
                print("Date of Birth:", info["Date of birth dd/mm/yyyy"])
                print("---------------------------")
                print("Subject:", info["Subject"])
                print("=========================")
    case 3:
        print("you have selected option 3")
        print("Here is the student data:")
        for key, info in students.items():
            print("=========================")
            print("ID:", info["ID"])
            print("---------------------------")
            print("Name:", info["Name"])
            print("---------------------------")
            print("Age:", info["Age"])
            print("---------------------------")
            print("Grade:", info["Grade"])
            print("---------------------------")
            print("Date of Birth:", info["Date of birth dd/mm/yyyy"])
            print("=========================")
        id=input("Enter the id of the student you want to update: ")
        updated = False
        for key, info in students.items():
            if info["ID"] == id:
                name=input("Enter the new name: ")
                age=int(input("Enter the new age: "))
                grade=input("Enter the new grade: ")
                date=input("Enter the new date of birth dd/mm/yyyy: ")
                students[key] = {"ID":id,"Name":name,"Age":age,"Grade":grade,"Date of birth dd/mm/yyyy":date}
                print("Student data updated successfully!")
                updated = True
                break
        if not updated:
            print("Student not found.")
    case 4:
        print("you have selected option 4")
        print("Here is the student data:")
        for key, info in students.items():
            print("=========================")
            print("ID:", info["ID"])
            print("---------------------------")
            print("Name:", info["Name"])
            print("---------------------------")
            print("Age:", info["Age"])
            print("---------------------------")
            print("Grade:", info["Grade"])
            print("---------------------------")
            print("Date of Birth:", info["Date of birth dd/mm/yyyy"])
            print("=========================")
        id=input("Enter the id of the student you want to delete: ")
        deleted = False
        for key, info in list(students.items()):
            if info["ID"] == id:
                del students[key]
                print("Student data deleted successfully!")
                deleted = True
                break
        if not deleted:
            print("Student not found.")
    case 5:
        print("you have selected option 5")
        if student:
            print("Here are the subjects for added students:")
            for info in student:
                print("=========================")
                print("ID:", info["ID"])
                print("Name:", info["Name"])
                print("Subject:", info["Subject"])
                print("=========================")
        else:
            print("No student subjects available.")
    case 6:
        print("you have selected option 6")
        print("Thank you for using our Student Data Organizer. Have a nice day!")
