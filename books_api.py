
import requests
import sqlite3


API_URL = "https://openlibrary.org/search.json?q=python"

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

try:
    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER
        )
    """)

    # Remove duplicates from earlier executions, if any
    cursor.execute("""
        DELETE FROM books
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM books
            GROUP BY title, author, COALESCE(publication_year, -1)
        )
    """)

    # Create a unique index
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_books
        ON books (
            title,
            author,
            COALESCE(publication_year, -1)
        )
    """)

    # Fetch API data
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()

    data = response.json()
    books = data.get("docs", [])[:20]

    inserted = 0

    for book in books:

        title = book.get("title", "Unknown")

        authors = book.get("author_name", [])
        author = ", ".join(authors) if authors else "Unknown"

        year = book.get("first_publish_year")

        # Ignore duplicate records
        cursor.execute("""
            INSERT OR IGNORE INTO books
            (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (title, author, year))

        inserted += cursor.rowcount

    conn.commit()

    print(f"New books inserted: {inserted}")

    # Display total records
    cursor.execute("SELECT COUNT(*) FROM books")
    total = cursor.fetchone()[0]

    print(f"Total books in database: {total}")

    # Display books
    cursor.execute("""
        SELECT id, title, author, publication_year
        FROM books
    """)

    print("\nBOOK DATABASE")

    for record in cursor.fetchall():
        print(record)

except (requests.exceptions.RequestException, sqlite3.Error) as error:
    conn.rollback()
    print("Error:", error)

finally:
    conn.close()
