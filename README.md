# Anchoor Mess Menu Management System

## Project Overview

**Anchoor Mess Menu Management System** is a simple Python-based console application designed to manage student records, mess attendance, extra charges, and monthly mess bills.

The system uses a Python dictionary to store student information and provides a menu-driven interface for performing common mess management operations.

## Features

The application provides the following features:

1. **Add Student**
   - Stores the student's roll number and name.
   - Initializes attendance and extra charges to zero.

2. **Mark Attendance**
   - Allows attendance to be recorded using the student's roll number.
   - Each successful attendance increases the student's attendance count by 1.

3. **Add Extra Amount**
   - Records an extra charge/unit for a student.
   - Each extra unit is charged at ₹20 during bill generation.

4. **Generate Monthly Bill**
   - Calculates the bill for every registered student.
   - Meal/attendance rate: **₹80 per attendance**.
   - Extra charge: **₹20 per extra unit**.

5. **Exit**
   - Closes the application.

## Billing Formula

The monthly bill is calculated using:

```text
Bill = (Attendance × ₹80) + (Extra Units × ₹20)
```

### Example

If a student has:

- Attendance = 20
- Extra Units = 3

Then:

```text
Bill = (20 × 80) + (3 × 20)
     = 1600 + 60
     = ₹1660
```

## Technologies Used

- **Programming Language:** Python 3
- **Interface:** Command-line / Console
- **Data Storage:** Python Dictionary
- **External Database:** Not required

## Data Structure

Student records are stored in the following format:

```python
students = {
    "101": {
        "name": "Student Name",
        "attendance": 20,
        "extra": 3
    }
}
```

Here:

- `roll` → Student roll number
- `name` → Student name
- `attendance` → Number of meals/attendance entries
- `extra` → Number of extra charge units

## How to Run

### 1. Install Python

Install Python 3 on your computer.

### 2. Save the Program

Save the source code as:

```text
main.py
```

### 3. Run the Program

Open a terminal or command prompt in the project folder and run:

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

## Menu

When the program starts, it displays:

```text
1. Add Student
2. Mark Attendance
3. Add Extra Amount
4. Generate Bill
5. Exit
```

Enter the corresponding number to perform an operation.

## Sample Usage

```text
1. Add Student
Enter your choice: 1
Enter Roll Number: 101
Enter Student Name: Rahul
Student added successfully!

Enter your choice: 2
Enter Roll Number: 101
Attendance marked successfully!

Enter your choice: 3
Enter Roll Number: 101
Extra amount added successfully!

Enter your choice: 4

----- Monthly Mess Bill -----
Rahul (101) - Rs. 100
-----------------------------
```

## Limitations

- Student data is stored only in memory.
- Data is lost when the program is closed.
- There is no login or authentication system.
- Attendance can currently be increased one entry at a time.
- The mess rate and extra charge are fixed in the source code.
- There is no graphical user interface.
- There is no database integration.

## Future Enhancements

The project can be extended by adding:

- File or database storage.
- Student record update and deletion.
- Monthly attendance reports.
- Payment status tracking.
- Customizable mess rates.
- Automatic monthly bill generation.
- Admin login.
- Search functionality.
- Graphical user interface using Tkinter.
- Export of bills to PDF or Excel.
- Separate records for different months.

## Project Structure

```text
Anchoor-Mess-Menu-Management-System/
│
├── main.py
├── README.md
└── STATEMENT.md
```

## Conclusion

The Anchoor Mess Menu Management System demonstrates the use of Python functions, dictionaries, loops, conditional statements, user input, and basic billing calculations to solve a practical mess-management problem.

It is suitable as a beginner-level Python project and can serve as a foundation for a more complete mess management application.
