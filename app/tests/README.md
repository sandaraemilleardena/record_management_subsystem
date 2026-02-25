# Record Management Subsystem

## Project Overview

The Record Management Subsystem is a Python-based application that allows users to manage records efficiently.  

It supports adding, updating, deleting, and searching records while ensuring proper validation and preventing duplicate IDs.

This project includes automated testing using Pytest and coverage reporting as required in SE102.

---

## Project Structure
record_management_subsystem/
│
├── app/
│ ├── record.py
│ ├── record_manager.py
│ └── record_validator.py
│
├── tests/
│ └── test_record.py
│
├── README.md
├── requirements.txt
└── .gitignore

---

## ⚙️ Features

✔ Add record  
✔ Delete record  
✔ Update record  
✔ Search record  
✔ Input validation  
✔ Prevent duplicate ID  
✔ Automated unit testing  
✔ Coverage report generation  

---

## System Components

### Record (record.py)
Represents a single record containing:
- record_id
- name
- age

### RecordValidator (record_validator.py)
Validates:
- ID must be integer and not None
- Name must not be empty
- Age must be integer and non-negative

### RecordManager (record_manager.py)
Handles:
- Adding records
- Searching records
- Updating records
- Deleting records
- Duplicate ID prevention

---

## 🧪 Testing

This project uses **pytest** for unit testing.

### Run Tests:
py -m pytest 
Expected Output:
==========test session starts =====================
platform win32 -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: D:\Acer\Desktop\record_management_subsystem
plugins: cov-7.0.0
collected 8 items

app\tests\test_record py ........                                                         [100%]

===== 8 passed in 0.07s ============


---

## Coverage Report

Generate coverage report:
py -m pytest --cov=app
Expected Coverage:
================= tests coverage ================
___ coverage: platform win32, python 3.14.3-final-0 ____

Name                       Stmts   Miss  Cover
----------------------------------------------
app\record.py                  9      1    89%
app\record_manager.py         22      1    95%
app\record_validator.py        6      0   100%
app\tests\test_record.py      37      0   100%
----------------------------------------------
TOTAL                         74      2    97%
============= 8 passed in 0.22s ==================


---

## Technologies Used

- Python 3
- Pytest
- Pytest-Cov
- Git
- GitHub
- Visual Studio Code

---

## Author

Student Name: Sandara Emille A. Ardena
              Joeren Trinidad
              Joana Marie Utinas
Course: SE102  
Project: Record Management Subsystem  

---

## Submission Status

✔ All required features implemented  
✔ All tests passed (8/8)  
✔ Coverage above 95%  
✔ Uploaded to GitHub  
✔ Ready for submission  