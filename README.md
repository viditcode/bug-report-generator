# Bug Report Generator 🐛

An AI-powered bug report generator built with Python and Streamlit. QA engineers can submit bugs through a modern web interface, get instant AI analysis powered by Google Gemini, and export reports to Excel and TXT formats.

---

## Live Demo
🚀 [Use App](https://bug-report-generator.streamlit.app/)

---

## What It Does

- Submit bug reports through a clean browser-based form
- Auto-generates Bug ID continuing from last session
- Records timestamp automatically with every bug
- Validates all inputs — no empty fields or invalid severity/priority
- Saves reports to `.txt` and `.xlsx` files without overwriting previous data
- View all bugs in a table with metrics and download options
- AI-powered bug analysis using Google Gemini — root cause, fix suggestions, edge cases

---

## Tech Stack
- Python
- Gemini API
- dotenv

---

## Project Structure

```
bug-report-generator/
│
├── app.py                      ← Streamlit web app (browser UI)
├── main.py                     ← Terminal version
├── requirements.txt            ← All dependencies
├── .env                        ← API keys (never push to GitHub!)
├── .gitignore
├── README.md
│
├── models/
│   ├── __init__.py
│   └── bug.py                  ← Bug class — data + auto ID + timestamp
│
├── views/
│   ├── __init__.py
│   └── report_view.py          ← Terminal report formatting
│
├── services/
│   ├── __init__.py
│   ├── file_services.py        ← Save to TXT and Excel
│   └── ai_services.py          ← Google Gemini AI analysis
│
└── utils/
    ├── __init__.py
    └── validator.py            ← Input validation functions
```

---

## How to Run 

**1. Clone the repo**
```bash
git clone https://github.com/viditcode/bug-report-generator.git
cd bug-report-generator
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up API key**

Create a `.env` file in the root folder:
```
AI_API_KEY=your_google_gemini_api_key_here
```

Get a free API key at: `aistudio.google.com`

**4. Run the web app**
```bash
streamlit run app.py
```

**Or run the terminal version**
```bash
python main.py
```

---

## Requirements

```
streamlit
openpyxl
pandas
google-genai
python-dotenv
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## Concepts Used

| Concept | Where Used |
|---|---|
| Variables & Data Types | Storing all bug fields |
| Loops + Nested Loops | Bug count and steps iteration |
| Lists — 1D & 2D arrays | `steps[]` and `all_bugs[]` storage |
| File handling | Writing `.txt` report with append mode |
| OOP — Class, `__init__`, `self` | `Bug`, `FileServices`, `AIService` classes |
| MVC Architecture | models, views, services, utils separation |
| Exception handling | `try/except` for file ops and AI calls |
| Input validation | `while True` loops with type checking |
| `datetime` library | Auto timestamp on every bug |
| Environment variables | Secure API key with `.env` |
| AI API integration | Google Gemini for bug analysis |

---

## Architecture — MVC Pattern

| Layer | File | Responsibility |
|---|---|---|
| Model | `models/bug.py` | Bug data, auto ID, timestamp |
| View | `views/report_view.py` | Terminal output formatting |
| Service | `services/file_services.py` | Save to TXT and Excel |
| Service | `services/ai_services.py` | AI analysis via Gemini |
| Utils | `utils/validator.py` | Input validation |
| Controller | `main.py` | Terminal flow control |
| Frontend | `app.py` | Streamlit web interface |

---

## Background

Built from scratch as a real-world QA automation project. I come from a manual QA background and built this tool to understand how Python can automate repetitive QA tasks — starting with a simple script and evolving it into a full MVC application with AI integration.

Every concept was learned by building, not by following tutorials.

---

## Author

**Vidit** — QA Engineer learning Python, SDET skills & AI integration
GitHub: [@viditcode](https://github.com/viditcode)

---

## Version History

| Version | What Changed |
|---|---|
| v1.0.0 | Basic bug report — single file, procedural code |
| v2.0.0 | OOP refactor — Bug class with methods |
| v3.0.0 | MVC file structure — models, views, services, utils |
| v4.0.0 | Validation, exception handling, auto Bug ID, timestamp, no overwrite |
| v5.0.0 | Streamlit web UI — 4 pages, metrics, download buttons |
| v6.0.0 | Google Gemini AI integration — bug analysis, root cause, fix suggestions |

---

## Release Notes

### v6.0.0 — AI Integration (Latest)
- Integrated Google Gemini AI for intelligent bug analysis
- New dedicated AI Analysis page — select any bug, get instant insights
- AI provides bug type, root cause, suggested fix, severity assessment and edge cases
- Senior QA engineer role prompt for accurate technical responses
- Secure API key management via `.env` and `python-dotenv`
- Exception handling for AI failures with graceful error messages
- `google-genai` and `python-dotenv` added as dependencies

### v5.0.0 — Streamlit Web UI
- Full browser-based interface using Streamlit
- Page 1: Report a Bug — form with all fields and validation
- Page 2: View Bug Reports — table with metrics and download buttons
- Page 3: Summary — latest bug with full details and downloads
- Metrics dashboard — total, critical, major, minor bug counts
- Download buttons for both Excel and TXT reports
- Version label displayed in sidebar
- `streamlit` and `pandas` added as dependencies

### v4.0.0 — Validation and Smart Features
- Input validation — severity and priority only accept valid values
- Exception handling — no crashes on invalid number input
- Auto-generated Bug ID (BUG-1, BUG-2...) continues from last session
- Timestamp recorded automatically with every bug using `datetime`
- Files no longer overwrite — append mode for TXT, load existing for Excel
- Excel headers auto-update when new fields added
- Counter derived from Excel row count — no separate counter file needed

### v3.0.0 — MVC File Structure
- Split single file into proper MVC architecture
- `models/bug.py` — Bug class, data only
- `views/report_view.py` — display formatting
- `services/file_services.py` — all file operations
- `utils/validator.py` — input validation functions
- `__init__.py` files added for proper Python packages
- Clean imports between all modules

### v2.0.0 — OOP Refactor
- Refactored entire codebase to Object Oriented Programming
- `Bug` class with `__init__`, `print_report`, `save_to_txt`, `save_to_excel`
- `self` used correctly for all attributes
- Objects created per bug instead of raw lists
- Clean import pattern with `from models.bug import Bug`

### v1.0.0 — Initial Release
- Takes multiple bug details as input from terminal
- Supports multiple steps to reproduce per bug
- Displays formatted bug report on screen
- Saves to `.txt` and `.xlsx` with proper column headers
- Loop handles multiple bugs per session

---

## Future Improvements

- [x] Auto-generate Bug ID ✅
- [x] Add timestamp to each bug report ✅
- [x] Prevent overwriting previous saved files ✅
- [x] Add input validation ✅
- [x] Add Streamlit GUI ✅
- [x] Integrate AI for bug analysis ✅
- [x] Deploy on Streamlit Cloud with live URL
- [ ] Export report to PDF format
- [ ] Add role-based access (reporter, assignee)
- [ ] Bug status tracking (Open, In Progress, Fixed, Closed)
- [ ] Java version with Selenium automation framework