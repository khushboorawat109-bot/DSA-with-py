# Student Management System in Python

students = {}

# Function to add student
def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!\n")


# Function to view all students
def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for roll, data in students.items():
        print(f"Roll No: {roll}")
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        print("----------------------")
    print()


# Function to search student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        print("\nStudent Found:")
        print(f"Name: {students[roll]['name']}")
        print(f"Marks: {students[roll]['marks']}\n")
    else:
        print("Student not found!\n")


# Function to update student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    if roll in students:
        name = input("Enter New Name: ")
        marks = float(input("Enter New Marks: "))

        students[roll]["name"] = name
        students[roll]["marks"] = marks

        print("Student updated successfully!\n")
    else:
        print("Student not found!\n")


# Function to delete student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")


# Main Menu
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

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
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.\n")