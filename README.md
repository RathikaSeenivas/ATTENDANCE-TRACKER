# 📊 Student Attendance Tracker System

A command-line based attendance management system built with Python. Designed to track student attendance subject-wise, calculate percentages, and alert students with low attendance — just like a real college system.

## 📌 Features

-  Add students and subjects dynamically
-  Mark attendance (Present / Absent / Leave) for any subject and date
-  View attendance record for a specific student (with subject-wise % and visual bar)
-  View class-wise attendance sheet (student vs date grid)
-  Overall attendance summary for all students
-  Low attendance alert — identifies students below 75% with action advice
-  Generate and save full attendance report to a `.txt` file
-  Auto-saves all data to JSON (no database required)
-  Prevents duplicate attendance marking for same subject & date

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Libraries:** `json`, `os`, `datetime` (all built-in — no pip install needed!)
- **Storage:** JSON file (`attendance_data.json`)
- **Concepts:** OOP, File I/O, List Comprehensions, Dictionary Operations, Modular Design

## 📂 Project Structure

```
attendance-tracker/
│
├── main.py                  # Entry point, menu loop, file save/load
├── attendance_manager.py    # Core class — all attendance logic
├── report.py                # Report generation module
├── attendance_data.json     # Auto-generated data file (after first run)
└── README.md
```

## ▶️ How to Run

### Requirements
- Python 3.6 or above
- No external libraries needed!

### Run:
```bash
python main.py
```

## 💻 Sample Output

```
==================================================
     📊 Student Attendance Tracker System
==================================================

✅ MARK ATTENDANCE
Subject: Python Programming | Date: 2024-08-15

  ECE001 - Rathika S    : P
  ECE002 - Priya R      : A
  ECE003 - Divya M      : P

✅ Attendance marked for 3 students!

──────────────────────────────────────────────────
📊 ATTENDANCE SUMMARY — ALL STUDENTS

  Roll       Name                 Present   Total       %  Status
  ─────────────────────────────────────────────────────────────
  ECE001     Rathika S                 18      20   90.0%  ✅ OK
  ECE002     Priya R                    8      20   40.0%  ⚠️ LOW
  ECE003     Divya M                   16      20   80.0%  ✅ OK

🚨 LOW ATTENDANCE ALERT:
  ⚠️  Priya R (ECE002)
     Attendance : 8/20 = 40.0%
     📧 ALERT   : Your attendance is below 75%!
     📌 ACTION  : Attend 22 more classes continuously to reach 75%.
```

## 🎯 Concepts Demonstrated

| Concept | Usage |
|---------|-------|
| Object-Oriented Programming | `AttendanceManager` class with methods |
| Modular Design | Separate `report.py` module |
| File I/O | JSON for persistent storage, `.txt` report export |
| List Comprehensions | Filtering records by roll/subject/date |
| Dictionary Operations | Student data management |
| Date & Time | `datetime` module for auto-dating |
| String Formatting | Aligned tables, progress bars |
| Input Validation | Loops until valid input is received |
| Algorithm | Calculates classes needed to reach 75% threshold |

## 👩‍💻 Author

Rathika S 
KGiSL Institute of Technology, Coimbatore  
