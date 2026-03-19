# Bug Report Generator 🐛

A Python command-line tool that collects bug details from a QA tester and automatically generates formatted reports in both `.txt` and `.xlsx` format.

Built as a real-world QA automation project to replace manual bug reporting.

---

## What It Does

- Takes multiple bug details as input from the user
- Supports multiple steps to reproduce per bug
- Displays a formatted bug report on screen
- Saves the report to a `.txt` file
- Saves the report to an Excel `.xlsx` file with proper column headers

---

## Demo

```
Enter the count of Bugs: 2

----------------------------------------
Please Enter Bug number: -1
Enter the Bug_Id: BUG-001
Enter the Bug_Summary: Login button not working on mobile
Enter the Bug_Description: App crashes when login button is tapped
Enter the Severity: Critical
Enter the Priority: P1
Enter the Environment: Android 13, Chrome 120
Enter the Bug_Label: Functional
Enter the number of Step: 2
Enter the step number 1: Open the app
Enter the step number 2: Tap the login button
----------------------------------------

========================================
        Bug Report
========================================
Bug ID:               BUG-001
Bug summary:          Login button not working on mobile
Bug Description:      App crashes when login button is tapped
Severity:             Critical
Priority:             P1
Environment:          Android 13, Chrome 120
Bug Type:             Functional
Steps to reproduce:
  1. Open the app
  2. Tap the login button
========================================
```

---

## Files Generated

| File | Description |
|---|---|
| `Bug_report.txt` | Formatted plain text report |
| `Bug_report.xlsx` | Excel sheet with column headers and one row per bug |

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/viditcode/bug-report-generator.git
cd bug-report-generator
```

**2. Install dependency**
```bash
pip install openpyxl
```

**3. Run the tool**
```bash
python Bug_Report_Generator.py
```

---

## Requirements

- Python 3.x
- openpyxl library

---

## Concepts Used

This project was built to practice and apply core Python concepts:

| Concept | Where Used |
|---|---|
| Variables & Data Types | Storing bug fields |
| `input()` | Taking user data |
| `for` loops | Iterating over bug count and steps |
| Nested loops | Collecting steps inside bug loop |
| Lists (1D & 2D) | `steps[]` and `all_bug[]` storage |
| File handling | Writing `.txt` report |
| Libraries | `openpyxl` for Excel output |

---

## Background

I come from a **manual QA background** and built this tool to understand how Python can automate repetitive QA tasks. This is my first Python automation project, built with a focus on understanding concepts rather than memorising syntax.

---

## Author

**Vidit** — QA Engineer learning Python & SDET skills  
GitHub: [@viditcode](https://github.com/viditcode)

---

## Future Improvements

- [ ] Add input validation (e.g. severity must be Critical/High/Medium/Low)
- [ ] Auto-generate Bug ID based on count
- [ ] Add timestamp to each bug report
- [ ] Export to PDF format
- [ ] Don't overwrite the previous data in the saved file
- [ ] Add the GUI 
- [ ] Add the AI like chatgpt to summaries the bug, find there root cause, how can we fix (not in details) and some more use.
