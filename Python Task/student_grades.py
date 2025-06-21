# 2. Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.

grades = {}

while True:
    print("\n1. Add/Update Student")
    print("2. View All Grades")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
        print(f"Grade updated for {name}")
    elif choice == "2":
        print("\nAll Student Grades:")
        for student, grade in grades.items():
            print(f"{student}: {grade}")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")