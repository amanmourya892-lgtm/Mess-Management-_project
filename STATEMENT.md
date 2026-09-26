# Project Statement

## Project Title

**Anchoor Mess Menu Management System**

## 1. Introduction

The Anchoor Mess Menu Management System is a Python-based console application developed to simplify the management of student mess attendance and monthly billing.

In a mess environment, maintaining student attendance and calculating individual bills manually can be time-consuming and may lead to calculation errors. This project provides a simple computerized solution for recording students, marking attendance, adding extra charges, and generating monthly bills.

## 2. Problem Statement

Manual management of mess records requires maintaining student details, attendance records, and extra charges separately. Calculating the monthly bill for each student manually can consume time and increase the possibility of errors.

Therefore, there is a need for a simple system that can:

- Maintain student records.
- Record daily/meal attendance.
- Record extra charges.
- Calculate individual monthly bills automatically.
- Display the bill for all registered students.

## 3. Objectives

The main objectives of the project are:

1. To create a simple student record management system.
2. To maintain student attendance records.
3. To record extra mess charges.
4. To automatically calculate monthly mess bills.
5. To reduce manual calculation and record-keeping work.
6. To provide an easy-to-use menu-driven interface.
7. To demonstrate fundamental Python programming concepts.

## 4. Proposed Solution

The proposed system uses a Python dictionary to maintain student information. Each student is identified using a unique roll number.

For every student, the system stores:

- Student name
- Attendance count
- Extra charge/unit count

The application provides menu options for adding students, marking attendance, adding extra charges, generating bills, and exiting the system.

## 5. Functional Requirements

### 5.1 Add Student

The system should allow the user to enter a student's roll number and name. A new student record is created with attendance and extra values initialized to zero.

### 5.2 Mark Attendance

The system should accept a roll number and increase the student's attendance count when the student exists in the system.

### 5.3 Add Extra Amount

The system should accept a roll number and increase the student's extra-unit count when the student exists.

### 5.4 Generate Bill

The system should calculate and display the bill of every registered student.

The billing formula is:

**Bill = (Attendance × ₹80) + (Extra Units × ₹20)**

### 5.5 Exit

The system should terminate when the user selects the Exit option.

## 6. Non-Functional Requirements

- The system should be simple and easy to operate.
- The program should provide clear messages for successful and unsuccessful operations.
- The program should respond to invalid menu choices.
- The system should use basic Python features without requiring external libraries.
- The application should be suitable for a beginner-level project.

## 7. Technology Requirements

### Hardware

- Computer or laptop
- Keyboard and monitor

### Software

- Python 3.x
- Any Python-compatible code editor or IDE
- Command Prompt/Terminal

## 8. Scope of the Project

The current version focuses on basic student and mess-billing management. It is designed primarily as a small console-based project.

The system can later be expanded to support:

- Persistent file/database storage
- Multiple months
- Payment tracking
- Admin authentication
- Student search and management
- Custom meal rates
- Reports and bill history
- PDF/Excel bill generation
- Graphical user interface

## 9. Expected Outcome

After implementing the project, the user will be able to:

- Add students to the system.
- Record student attendance.
- Record extra charges.
- Generate the calculated monthly bill for each student.
- Manage basic mess billing operations through a simple console interface.

## 10. Conclusion

The Anchoor Mess Menu Management System provides a simple solution for managing student mess attendance and billing. The project demonstrates practical use of Python dictionaries, functions, loops, conditional statements, input handling, and arithmetic operations.

The project can be further developed into a complete mess management system by adding permanent data storage, authentication, reports, payment tracking, and a graphical user interface.
