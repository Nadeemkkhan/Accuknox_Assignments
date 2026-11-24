
import requests
import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


# API endpoint
API_URL = "http://127.0.0.1:5000/students"


# Fetch data from API
response = requests.get(API_URL, timeout=10)
response.raise_for_status()

students = response.json()


# Convert JSON into DataFrame
df = pd.DataFrame(students)


# Validate data
if df.empty:
    raise ValueError("No student data received")

if not {"name", "score"}.issubset(df.columns):
    raise ValueError("Missing required columns")

df["score"] = pd.to_numeric(df["score"], errors="raise")


# Calculate average score
average_score = df["score"].mean()

print("\nSTUDENT SCORE REPORT")
print("-" * 40)

print(df.to_string(index=False))

print("-" * 40)

print("Average Score:", round(average_score, 2))


# Create bar chart
plt.figure(figsize=(9, 5))

plt.bar(
    df["name"],
    df["score"],
    label="Student Score"
)

# Average reference line
plt.axhline(
    y=average_score,
    linestyle="--",
    label=f"Average: {average_score:.2f}"
)

plt.xlabel("Students")
plt.ylabel("Test Scores")

plt.title("Student Test Score Analysis")

plt.legend()
plt.tight_layout()

# Save chart
plt.savefig("student_scores.png")

# Save chart
plt.savefig("student_scores.png", dpi=300)

print("\nChart saved successfully as student_scores.png")