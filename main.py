import sqlite3

import pandas as pd

# Connect database

conn = sqlite3.connect("school.db")

# Create cursor

cursor = conn.cursor()

print("Database connected!")

# Create table

cursor.execute("""

CREATE TABLE IF NOT EXISTS Students (

id INTEGER PRIMARY KEY,

name TEXT,

age INTEGER,

marks INTEGER

)

""")

print("Table created!")

# Insert data

cursor.execute("INSERT INTO Students (name, age, marks) VALUES ('Ali', 13, 85)")

cursor.execute("INSERT INTO Students (name, age, marks) VALUES ('Ahmed', 14, 90)")

cursor.execute("INSERT INTO Students (name, age, marks) VALUES ('Sara', 13, 95)")

# Save changes

conn.commit()

print("Data inserted!")

# Read table using pandas

students = pd.read_sql(

"""

SELECT * FROM Students;

""",

conn,

)

print("\nStudent Data:\n")

print(students)

# Show table info

print("\nDataset Info:\n")

print(students.info())

# Close connection

conn.close()
