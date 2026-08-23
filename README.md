# 📊 Marks Analyser V5

A desktop application built in Python to manage student marks, analyse academic performance, generate reports, and visualize progress using graphs.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Matplotlib](https://img.shields.io/badge/Graphs-Matplotlib-red)

## Overview

Marks Analyser V5 is the final version of a project that evolved from a simple percentage calculator into a complete student performance management system. It stores data in SQLite, provides a graphical interface with Tkinter, and creates visual insights using Matplotlib.

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

## Learning Outcomes

Through this project I learned:

- Object-oriented program structure
- SQLite database management
- GUI development with Tkinter
- Data visualization using Matplotlib
- Unit testing with Python
- Modular software architecture

## Author

**Tanishq Hardeniya**

Independent Python Project
