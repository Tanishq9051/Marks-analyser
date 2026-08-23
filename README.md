# 📊 Marks Analyser

A modular Python student-performance management application developed progressively from a basic marks calculator into a database-driven desktop application with analysis, visualization, reporting, GUI, and automated testing.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Matplotlib](https://img.shields.io/badge/Graphs-Matplotlib-red)

## 🎯 Project Overview

Marks Analyser was developed as a progressive software project.

Instead of building the final application at once, the project was developed through multiple versions, with each version introducing new programming concepts and functionality.

The final V5 application can:

- Manage multiple students
- Store multiple examinations for each student
- Validate marks before storing them
- Calculate percentages automatically
- Analyse subject-wise performance
- Identify strongest and weakest subjects
- Compare examination performance
- Track performance across examinations
- Generate performance graphs
- Rank students based on performance
- Generate student reports
- Store information persistently using SQLite
- Provide a graphical desktop interface
- Run automated tests for core functionality

---

## 🚀 Current Version — V5

V5 combines:

**Database + Analysis + Visualization + Reporting + GUI + Testing**

The application uses a modular structure where different responsibilities are separated into different Python files.

---

## ✨ Features

### 👨‍🎓 Student Management

- Add students
- Search students
- View student records
- Delete students
- Automatically remove associated examination data

### 📝 Examination Management

- Add examinations for students
- Store maximum marks for each subject
- Store obtained marks
- Validate marks
- Update examination records
- Delete examinations
- View examination history

### 📈 Performance Analysis

- Calculate examination percentages
- Calculate overall student averages
- Calculate subject averages
- Identify strongest subject
- Identify weakest subject
- Classify performance
- Compare examinations
- Calculate class rankings
- Calculate class statistics

### 📊 Data Visualization

Matplotlib is used to generate visual representations of:

- Examination performance
- Subject performance
- Examination comparisons
- Performance trends

### 📄 Report Generation

The application can generate student performance reports containing:

- Student information
- Overall average
- Performance classification
- Strongest subject
- Weakest subject
- Subject averages
- Examination history

Reports can be exported as `.txt` files.

### 🗄️ Database

Student and examination information is stored using SQLite.

The database uses a relationship between students and their examinations:
Each examination is associated with a student using a foreign key.

## Features

- Add and manage students
- Record multiple exams for each student
- Automatic percentage calculation
- Subject-wise performance analysis
- Strongest and weakest subject detection
- Compare two exams
- Performance progress graphs
- Subject average graphs
- Export student report (.txt)
- Student ranking system
- Search students instantly

## Technologies Used

- Python 3
- Tkinter (GUI)
- SQLite3 (Database)
- Matplotlib (Data Visualization)
- Unittest (Testing)

## Project Structure

```text
Marks_Analyser/
│
├── app.py                 # Entry point
├── gui.py                 # Graphical interface
├── database.py            # SQLite operations
├── analysis.py            # Performance calculations
├── reports.py             # Report generation
├── visualization.py       # Graphs
├── requirements.txt
├── .gitignore
│
├── tests/
│   ├── test_analysis.py
│   └── test_reports.py
│
└── screenshots/
```

                 app.py
                   │
                   ▼
                 gui.py
              ┌────┼────┐
              ▼    ▼    ▼
        database  analysis  visualization
              │      │          │
              ▼      ▼          ▼
           SQLite  Results    Matplotlib
                    │
                    ▼
                 reports


## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

Current automated test status:

- Analysis module ✔
- Report generation ✔

**Total: 7 passing tests**

## Version History

| Version | Description |
|----------|-------------|
| V1 | Percentage calculator |
| V2 | Multi-student support |
| V3 | SQLite database integration |
| V4 | Performance analytics & rankings |
| **V5** | GUI, graphs, reports, polished architecture |

📸 Screenshots

Screenshots demonstrating the V5 application are available in the screenshots folder.

They show the graphical interface, student management, examination history, analysis and visualization features.

## Learning Outcomes

Through this project I learned:

- Object-oriented program structure
- SQLite database management
- GUI development with Tkinter
- Data visualization using Matplotlib
- Unit testing with Python
- Modular software architecture

## Possible Future Improvements

Possible future improvements include:

PDF report generation
CSV data export
Support for additional subjects
Attendance tracking
User authentication
Improved GUI design
More extensive automated test coverage
Database backup and restore
Advanced statistical analysis

These features are outside the current V5 scope.

## Current Limitations
The application is designed as a local desktop application.
The current academic model focuses on Physics, Chemistry and Biology.
Reports are currently exported as text files.
Automated tests focus primarily on core logic and report generation rather than GUI interaction.
SQLite is used as a local database rather than a remote database server.

## Author

**Tanishq Hardeniya**

Independent Python Project
