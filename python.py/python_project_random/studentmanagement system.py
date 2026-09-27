students = {}
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Student Name: ")
    try:
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Invalid input!")
        return
    students[roll] = {
        "name": name,
        "age": age,
        "marks": marks
    }
    print("Student added successfully!")
def view_students():
    if len(students) == 0:
        print("No student records found!")
        return
    print("\n===== STUDENT LIST =====")
    for roll, data in students.items():
        print("\n----------------------")
        print("Roll Number:", roll)
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Marks:", data["marks"])
def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        data = students[roll]
        print("\nStudent Found!")
        print("Roll Number:", roll)
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Marks:", data["marks"])
    else:
        print("Student not found!")
def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll not in students:
        print("Student not found!")
        return
    print("Leave blank if you don't want to change.")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    marks = input("Enter new marks: ")
    if name:
        students[roll]["name"] = name
    if age:
        students[roll]["age"] = int(age)
    if marks:
        students[roll]["marks"] = float(marks)
    print("Student updated successfully!")
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")
def show_topper():
    if len(students) == 0:
        print("No student records found!")
        return
    topper_roll = max(
        students,
        key=lambda x: students[x]["marks"]
    )
    topper = students[topper_roll]
    print("\n===== CLASS TOPPER =====")
    print("Roll Number:", topper_roll)
    print("Name:", topper["name"])
    print("Marks:", topper["marks"])
# main program
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    
    print("welcome to the student management system")
    print("1.add student")
    print("2.view students")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.show topper")
    print("7.exit")
    choice = input("enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_topper()
    elif choice == "7":
        print("exiting program   thank you for using the student management system")
        break
    else:
        print("invalid choice  please try again")

    