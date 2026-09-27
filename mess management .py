# Anchoor Mess Menu Management System:
students = {}

#add_students():
roll = input("Enter Roll Number: ")
name = input("Enter Student  Name: ")
students[roll] = {"name": name, "attendance": 0, "extra": 0}
print("Student added successfully!\n")

# mark_attendance():
roll = input("Enter Roll Number: ")
if roll in students:
        students[roll]["attendance"] += 1
        print("Attendance marked successfully!\n")
else:
        print("Student not found!\n")

#add_extra():
roll = input("Enter Roll Number: ")
if roll in students:
    students[roll]["extra"] += 1
    print("Extra amount added successfully!\n")
else:
    print("Student not found!\n")

# generate_bill():
    mess_rate = 80  # per meal/day
    print("\n----- Monthly Mess Bill -----")
    for roll, data in students.items():
        bill = (data["attendance"] * mess_rate) + (data["extra"] * 20)  # Assuming extra is charged at 20 per unit
        print(f"{data['name']} ({roll}) -Rs. {bill}")
    print("-----------------------------\n")

while True:
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Add Extra Amount")
    print("4. Generate Bill")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_students()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        add_extra()
    elif choice == "4":
        generate_bill()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.\n")