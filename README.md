# Python and SQLite Assignment

This project demonstrates Python programming, REST API integration, data analysis, CSV processing, and SQLite database operations.

## Tasks Completed

### Task 1: Fetch Book Data from an API
- Fetches book information from the Open Library API.
- Uses Python `requests` to retrieve JSON data.
- Stores book details in an SQLite database (`books.db`).
- Displays stored records.

### Task 2: Student Score Analysis
- Creates a sample REST API using Flask.
- Fetches student scores using Python `requests`.
- Uses Pandas to process student data.
- Calculates the average score.
- Generates a bar chart using Matplotlib.
- Saves the chart as `student_scores.png`.

**Note:** The student API is a locally created sample API for demonstrating REST API integration.

### Task 3: CSV to SQLite
- Reads user information from `users.csv`.
- Uses Python's built-in CSV module.
- Inserts records into an SQLite database (`users.db`).
- Uses a unique email constraint to prevent duplicate records.

## Technologies Used
- Python
- SQLite
- Flask
- Requests
- Pandas
- Matplotlib
- CSV

## Project Setup

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Assignment_1
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Programs

**Task 1:**
```bash
python books_api.py
```

**Task 2:** Start the API in one terminal:
```bash
python student_api.py
```

Then run the analysis in another terminal:
```bash
python student_analysis.py
```

**Task 3:**
```bash
python csv_to_sqlite.py
```

## Project Output
- `books.db` – Book records
- `student_scores.png` – Student score chart
- `users.db` – User records
