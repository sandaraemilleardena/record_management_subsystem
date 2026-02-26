# Record Management Subsystem


# Project Overview

The Record Management Subsystem is a Python-based application that allows users to manage records efficiently.

It supports:

Adding records

Updating records

Deleting records

Searching records

Preventing duplicate IDs

Input validation

The system includes:

Backend logic written in Python

SQLite database integration

Automated testing using Pytest

Coverage reporting

A Web-Based Dashboard UI using HTML, Bootstrap (CSS), and script functionality

## Project Structure
record_management_subsystem/
│
├── app/
│   ├── record.py
│   ├── record_manager.py
│   ├── record_validator.py
│   ├── static/
│   └── templates/
│       └── dashboard.html
│
├── tests/
│   └── test_record.py
│
├── app.py
├── records.db
├── requirements.txt
└── README.md

---

## Features

Add record
Delete record
Update record
Search record
Input validation
Prevent duplicate ID
Automated unit testing
Coverage report generation
Web-based dashboard interface
Bootstrap responsive UI 

---

## System Components

1. Record (record.py)

Represents a single record containing:

record_id
name
age

Raises ValueError for invalid input.

2️. RecordValidator (record_validator.py)

Validates:
ID must be integer and not None
Name must not be empty or whitespace
Age must be integer and non-negative

3️. RecordManager (record_manager.py)

Handles:

Adding records
Updating records
Deleting records
Searching records
Retrieving all records
Duplicate ID prevention
Database interaction (SQLite)

## Web Dashboard

The system includes a web-based dashboard interface built using:

HTML5
Bootstrap 5 (CSS Framework)
Basic JavaScript confirmation
Flask templating (Jinja2)
Dashboard Capabilities

Add Record Form
Update Record Form
Search Record Form
Display All Records in Table
Delete Button with Confirmation
Flash Message Notifications
Responsive Layout

The dashboard provides a user-friendly interface to interact with the backend Record Management System.

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

app\tests\test_record.py ........                                                                [100%]

===== 8 passed in 0.13s ============


---

## Coverage Report

Generate coverage report:
py -m pytest --cov=app
Expected Coverage:
================= tests coverage ================
___ coverage: platform win32, python 3.14.3-final-0 __________________ 

Name                       Stmts   Miss  Cover
----------------------------------------------
app\__init__.py                0      0   100%
app\record.py                  9      1    89%
app\record_manager.py         18      1    94%
app\record_validator.py       18     10    44%
app\tests\test_record.py      37      0   100%
----------------------------------------------
TOTAL                         82     12    85%
============= 8 passed in 0.22s ==================


---

## Technologies Used

- Python 3
- SQLite
- Pytest
- Pytest-Cov
- HTML5
- Bootstrap 5
- JavaScript
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
