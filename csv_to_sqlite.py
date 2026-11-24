
import csv
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER
    )
""")

# Read CSV and insert records
inserted_count = 0

with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO users (name, email, age)
                VALUES (?, ?, ?)
            """, (row["name"], row["email"], int(row["age"])))

            inserted_count += cursor.rowcount

        except (ValueError, KeyError) as error:
            print(f"Skipping invalid row: {row}. Reason: {error}")

# Save changes
connection.commit()

print(f"Successfully inserted {inserted_count} users.")

# Display stored users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("\nUsers stored in database:")
for user in users:
    print(user)

connection.close()
