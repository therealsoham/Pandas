import sqlite3

import pandas as pd

# Connect to database

conn = sqlite3.connect("sales.db")

cursor = conn.cursor()

# Create table

cursor.execute("""

CREATE TABLE sales (

id INTEGER,

product TEXT,

category TEXT,

price INTEGER

)

""")

# Insert values

data = [

(1, "iPhone", "Electronics", 1000),

(2, "Laptop", "Electronics", 1200),

(3, "iPhone", "Electronics", 1000),

(4, "Bread", "Grocery", 5),

(5, "Milk", "Grocery", 10),

(6, "Laptop", "Electronics", 1200),

]

cursor.executemany("INSERT INTO sales VALUES (?,?,?,?)", data)

conn.commit()

# Load SQL table into DataFrame

df = pd.read_sql_query("SELECT * FROM sales", conn)

summary = df.groupby("category")["price"].sum()

print(summary)