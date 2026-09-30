<div align="center">

# 💼 Employee Payroll Management System

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=28&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=800&lines=Employee+Management;Payroll+Management;Salary+Calculation;Python+Desktop+Application" alt="Typing SVG" />

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Tkinter-GUI-FFB000?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/Payroll-Management-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>

<br><br>

*A Python-based desktop application for managing employee information, calculating salaries, maintaining payroll records and generating salary receipts using Tkinter and SQLite.*

</div>

---

# 📖 Project Overview

**Employee Payroll Management System** is a Python-based desktop application developed to manage employee information and payroll-related operations.

The system provides a graphical user interface using **Tkinter** and stores employee and salary information in an **SQLite database**.

The application allows users to maintain employee records, calculate monthly salaries, manage attendance-related deductions, update employee information and generate salary receipts.

The project demonstrates practical implementation of Python GUI development, database management, employee record management, salary calculation and payroll processing.

---

# 🎯 Objectives

* Develop a desktop-based employee payroll management system.
* Store and manage employee information.
* Maintain employee salary records.
* Calculate monthly employee salaries.
* Calculate total working days according to month and year.
* Manage employee absence information.
* Apply medical, PF and convenience-related salary values.
* Generate net salary.
* Search employee records.
* Update and delete employee information.
* Generate salary receipts.
* Store payroll information using SQLite.
* Provide a simple and user-friendly graphical interface.

---

# ✨ Project Highlights

* ✔ Python-based desktop application.
* ✔ Tkinter graphical user interface.
* ✔ SQLite database integration.
* ✔ Employee information management.
* ✔ Employee search functionality.
* ✔ Employee record creation.
* ✔ Employee record updating.
* ✔ Employee record deletion.
* ✔ Monthly payroll management.
* ✔ Salary calculation.
* ✔ Automatic total-day calculation.
* ✔ Absence management.
* ✔ Medical deduction/amount handling.
* ✔ PF management.
* ✔ Convenience amount handling.
* ✔ Net salary calculation.
* ✔ Salary receipt generation.
* ✔ Salary receipt printing.
* ✔ Employee status management.
* ✔ Employee experience management.
* ✔ Date of Birth and Date of Joining fields.
* ✔ Input validation.
* ✔ Login system.
* ✔ Password reset through OTP.
* ✔ User data management.

---

# 🛠️ Technologies Used

| Technology      | Purpose                    |
| --------------- | -------------------------- |
| Python          | Application Development    |
| Tkinter         | Graphical User Interface   |
| SQLite          | Database Management        |
| Pillow (PIL)    | Image Processing           |
| tkcalendar      | Date Selection             |
| Calendar        | Working-Day Calculation    |
| SMTP            | Email / OTP Functionality  |
| OS Module       | File and System Management |
| Temporary Files | Receipt / Print Processing |

---

# 📂 Project Structure

```text
Employee-Payroll-Management/
│
├── create_db.py
├── employee.py
├── login.py
├── Delete record.py
├── email_pass.py
│
├── emp.db
├── user_data.txt
│
├── salary_receipts/
│   ├── 1.txt
│   └── 2.txt
│
├── Image/
│   ├── Cat.jpg
│   ├── Cat2.jpg
│   ├── Category.jpg
│   ├── Image1.jpg
│   ├── Image2.jpeg
│   ├── Image3.jpeg
│   ├── Image4.jpeg
│   ├── Image5.jpeg
│   ├── Image6.jpg
│   ├── Image7.jpg
│   ├── Image8.jpg
│   ├── Login.jpg
│   ├── Logo.png
│   ├── Menu.png
│   ├── phones.png
│   ├── signup.png
│   ├── socialmedia.png
│   └── srms.jpg
│
├── Documentation.pdf
├── Employee Payroll Management System.pptx
├── Trial.docx
├── Trial.py
├── Sample.py
├── sample code.py
│
└── README.md
```

---

# 🗃️ Database Information

The project uses an SQLite database named:

```text
emp.db
```

The database contains the payroll table:

```text
e_salary
```

| Property             | Details             |
| -------------------- | ------------------- |
| Database Name        | `emp.db`            |
| Database Type        | Relational Database |
| DBMS                 | SQLite              |
| Programming Language | Python              |
| GUI Framework        | Tkinter             |
| Main Table           | `e_salary`          |

---

# 🗄️ Employee Salary Table

The `e_salary` table stores both employee information and payroll information.

| Field          | Description                |
| -------------- | -------------------------- |
| emp_code       | Unique Employee Code       |
| designation    | Employee Designation       |
| name           | Employee Name              |
| age            | Employee Age               |
| gender         | Employee Gender            |
| email          | Employee Email             |
| hr_location    | Hiring / HR Location       |
| dob            | Date of Birth              |
| doj            | Date of Joining            |
| proof_id       | Identity Proof             |
| contact        | Contact Number             |
| status         | Employee Status            |
| experience     | Work Experience            |
| address        | Employee Address           |
| month          | Salary Month               |
| year           | Salary Year                |
| basic_salary   | Basic Salary               |
| total_days     | Total Days in Month        |
| absent         | Number of Absent Days      |
| medical        | Medical Amount             |
| pf             | PF Amount                  |
| convence       | Convenience Amount         |
| net_salary     | Calculated Net Salary      |
| salary_reciept | Salary Receipt Information |

---

# 👨‍💼 Employee Management

The Employee Management module allows users to maintain employee records.

### Employee Information

The system stores:

* Employee Code
* Designation
* Name
* Age
* Gender
* Email
* Contact
* Date of Birth
* Date of Joining
* Proof ID
* Hiring / HR Location
* Employee Status
* Experience
* Address

### Operations

* Add employee
* Update employee
* Delete employee
* Search employee
* Clear employee information

---

# 💰 Payroll Management

The payroll section allows users to calculate and manage employee salary information.

The system provides fields for:

* Salary Month
* Salary Year
* Basic Salary
* Total Days
* Absent Days
* Medical
* PF
* Convenience
* Net Salary

The payroll information is stored in the SQLite database.

---

# 🧮 Salary Calculation

The system includes a salary calculation feature.

The user can enter:

```text
Basic Salary
Total Working Days
Absent Days
Medical
PF
Convenience
```

The application processes the entered payroll information and generates the **Net Salary**.

The calculation is performed through the application's Python logic.

---

# 📅 Working-Day Calculation

The application uses Python's **calendar** functionality to determine the number of days in a selected month and year.

For example:

```text
January → 31 Days
February → 28/29 Days
March → 31 Days
April → 30 Days
```

The total number of days is automatically updated when the month or year is changed.

---

# 🧑‍💼 Employee Details

The application supports several employee-related fields.

### Designation

Stores the employee's job designation.

### Date of Birth

The system uses a date picker to select the employee's date of birth.

### Date of Joining

Stores the employee's joining date.

### Age

The system calculates employee age based on the Date of Birth.

### Experience

Employee experience can be entered using a Spinbox.

### Gender

The available options include:

```text
Male
Female
Other
```

### Proof ID

The system provides options such as:

```text
Aadhar Card
Pan Card
License
```

### Status

Employee status can be selected as:

```text
Active
Inactive
```

---

# 🔍 Search Functionality

The application includes employee search functionality.

Users can search employee records using the available employee information and retrieve stored records from the SQLite database.

Search results are displayed within the application interface.

---

# 🔄 CRUD Operations

The Employee Payroll Management System implements CRUD operations.

| Operation | Description                          |
| --------- | ------------------------------------ |
| Create    | Add new employee/payroll records     |
| Read      | Display stored employee records      |
| Update    | Modify existing employee information |
| Delete    | Remove employee records              |

These operations are connected to the SQLite database.

---

# 🧾 Salary Receipt

The application provides functionality for generating salary receipts.

Salary receipt information includes details such as:

```text
Employee ID
Salary Month
Generated Date
Total Days
Present / Absent Days
Medical
PF
Convenience
Gross Payment
Net Salary
```

The project maintains salary receipt files inside:

```text
salary_receipts/
```

---

# 🖨️ Print Functionality

The payroll system includes a **Print** option for salary information.

The print functionality prepares the salary information and processes it for printing.

The system also uses temporary files during receipt/printing operations.

---

# 🔐 Login System

The project includes a separate login application.

The login screen provides:

* Username
* Password
* Login button
* Forgot Password functionality
* Sign-up interface

The system checks the entered username and password before opening the employee payroll application.

---

# 🔑 Password Reset

The application provides a password reset workflow using OTP.

The process includes:

```text
Enter Registered Email
        ↓
Send OTP
        ↓
Enter OTP
        ↓
Verify OTP
        ↓
Enter New Password
        ↓
Confirm Password
        ↓
Password Reset
```

The application uses Python's SMTP functionality for sending the OTP through email.

---

# 📧 Email & OTP Functionality

The login system uses:

```python
smtplib
```

to communicate with an SMTP server.

A random six-digit OTP is generated for password reset verification.

Example:

```text
OTP → 123456
```

The OTP is then verified before allowing the user to reset the password.

> **Security Note:** Never upload real email passwords, SMTP credentials, API keys or app passwords to a public GitHub repository.

---

# 🖥️ User Interface

The application uses **Tkinter** to create its graphical interface.

Major interface components include:

* Login Window
* Employee Information Form
* Salary Details Form
* Search Section
* Employee Records Table
* Salary Calculation Section
* Salary Receipt Section
* Buttons
* Entry Fields
* ComboBoxes
* Date Pickers
* Spinboxes
* Message Boxes

---

# 🔑 Python Concepts Used

The project demonstrates several Python programming concepts:

* Variables
* Functions
* Classes
* Object-Oriented Programming
* Conditional Statements
* Loops
* Exception Handling
* File Handling
* Database Connectivity
* GUI Programming
* Event Handling
* Modules and Imports
* Input Validation

---

# 🗄️ Database Concepts Used

The project demonstrates:

* SQLite database creation
* Table creation
* Primary Keys
* INSERT operations
* SELECT operations
* UPDATE operations
* DELETE operations
* Database queries
* Database connectivity

---

# 🧩 Python Libraries Used

### Tkinter

Used to create the graphical user interface.

### SQLite3

Used to create and manage the employee payroll database.

### Pillow

Used for loading, resizing and displaying images in the GUI.

### tkcalendar

Used to provide date selection through calendar widgets.

### Calendar

Used to calculate the number of days in a selected month.

### SMTP

Used for email-based OTP functionality.

### OS

Used for file and directory operations.

### Temporary Files

Used during receipt and printing operations.

---

# 🏗️ Application Architecture

The project follows a modular desktop application structure.

```text
                    ┌───────────────────┐
                    │    Login System   │
                    └─────────┬─────────┘
                              │
                     Authentication
                              │
                              ▼
                ┌─────────────────────────┐
                │ Employee Payroll System │
                └────────────┬────────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
   Employee Details    Salary Details      Search Records
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Salary Calculate│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Salary Receipt  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   SQLite DB     │
                    │     emp.db      │
                    └─────────────────┘
```

---

# 🚀 How to Run

## Step 1 — Install Python

Install Python 3.x.

Check the installation:

```bash
python --version
```

---

## Step 2 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd Employee-Payroll-Management
```

---

## Step 3 — Install Required Libraries

Install the required packages:

```bash
pip install pillow tkcalendar
```

Tkinter is normally included with standard Python installations on Windows.

---

## Step 4 — Create the Database

Run:

```bash
python create_db.py
```

This creates the SQLite database:

```text
emp.db
```

and the required:

```text
e_salary
```

table.

---

## Step 5 — Start the Login System

Run:

```bash
python login.py
```

The login window will open.

---

## Step 6 — Login

Enter the configured username and password.

After successful authentication, the Employee Payroll Management System will open.

---

# 📌 Default Login

The current project contains a default fallback login in the login code.

```text
Username: Student
Password: 123456
```

> **Important:** Change default credentials before publishing or using the application in a real environment.

---

# 📁 Important Files

| File                                      | Purpose                           |
| ----------------------------------------- | --------------------------------- |
| `login.py`                                | Login and password reset system   |
| `employee.py`                             | Main employee payroll application |
| `create_db.py`                            | Creates SQLite database and table |
| `emp.db`                                  | SQLite database                   |
| `user_data.txt`                           | Stores login information          |
| `email_pass.py`                           | Email configuration               |
| `salary_receipts/`                        | Stores salary receipt files       |
| `Image/`                                  | Application images                |
| `Documentation.pdf`                       | Project documentation             |
| `Employee Payroll Management System.pptx` | Project presentation              |

---

# 📌 Important Security Notes

Before uploading this project to a **public GitHub repository**, remove or replace sensitive information.

Do **not** upload:

```text
Real email passwords
SMTP App Passwords
Real user passwords
Personal employee information
Private database records
```

The project currently contains email credential-related files and login data, so these should be replaced with placeholders or environment variables before making the repository public.

A safer approach is:

```text
.env
```

for local credentials and add `.env` to:

```text
.gitignore
```

---

# 🎓 Learning Outcomes

After completing this project, I gained practical experience in:

* Python programming.
* Object-Oriented Programming.
* Tkinter GUI development.
* SQLite database management.
* CRUD operations.
* Employee record management.
* Payroll processing.
* Salary calculation.
* Date and calendar handling.
* Input validation.
* File handling.
* Receipt generation.
* Printing functionality.
* Email and OTP integration.
* User authentication.
* Password reset functionality.
* Modular Python programming.
* Desktop application development.

---

# 💼 Skills Demonstrated

### Programming Skills

* Python
* Object-Oriented Programming
* Exception Handling
* File Handling
* Modular Programming

### GUI Development

* Tkinter
* Forms
* Buttons
* Labels
* Entry Fields
* ComboBoxes
* Date Pickers
* Spinboxes
* Tables
* Message Boxes

### Database Skills

* SQLite
* Database Creation
* Table Design
* CRUD Operations
* SQL Queries
* Database Connectivity

### Payroll Skills

* Employee Management
* Salary Management
* Attendance Handling
* Salary Calculation
* Payroll Records
* Salary Receipt Generation

### Additional Skills

* Email Integration
* OTP Verification
* Password Reset
* Input Validation
* File Management

---

# 🏆 Project Achievements

✅ Developed a complete Employee Payroll Management System.

✅ Created a graphical user interface using Tkinter.

✅ Integrated SQLite database for employee and payroll records.

✅ Implemented employee information management.

✅ Implemented employee search functionality.

✅ Implemented employee record update and deletion.

✅ Implemented monthly salary management.

✅ Implemented salary calculation.

✅ Added automatic month/day handling.

✅ Added employee absence management.

✅ Added PF, medical and convenience fields.

✅ Implemented net salary calculation.

✅ Added salary receipt generation.

✅ Added printing functionality.

✅ Developed login authentication.

✅ Added OTP-based password reset functionality.

---

# 🔮 Future Enhancements

The system can be further improved by adding:

### 🔐 Security Enhancements

* Password hashing using `bcrypt`.
* Secure authentication.
* Role-Based Access Control.
* Environment variables for credentials.
* Session management.
* Secure OTP expiration.
* Login attempt limits.

### 💰 Payroll Enhancements

* Automatic tax calculation.
* Professional payslip generation.
* Overtime calculation.
* Bonus management.
* Allowance management.
* Deduction management.
* Salary history.
* Monthly payroll reports.

### 📊 Reporting Enhancements

* Employee salary reports.
* Monthly payroll reports.
* Department-wise reports.
* Salary statistics.
* Graphs and charts.
* PDF payslip generation.
* Excel payroll export.

### ☁️ System Enhancements

* Cloud database integration.
* Multi-user support.
* Web-based payroll system.
* Mobile-friendly interface.
* Automated database backup.
* Online employee portal.

---

# 📌 Project Summary

**Employee Payroll Management System** is a Python-based desktop application developed to manage employee information and payroll operations.

The project combines **Python, Tkinter and SQLite** to provide employee record management, salary calculation, payroll processing, salary receipt generation and authentication functionality.

It demonstrates how Python can be used to build a practical desktop application that combines **GUI development, database management, employee management and payroll processing**.

---

# 👨‍💻 Author

## Sarth Thakar
