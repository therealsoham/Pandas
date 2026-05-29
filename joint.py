# Import Necessary Libraries

import pandas as pd

import sqlite3

# ---------------- DATABASE COpypytNNECTION ----------------

database = "database.sqlite"

conn = sqlite3.connect(database)

cursor = conn.cursor()

# ---------------- CREATE TABLES ----------------

# Country Table

cursor.execute("""

CREATE TABLE IF NOT EXISTS country (

Country_Id INTEGER PRIMARY KEY,

Country_Name TEXT

)

""")

# City Table

cursor.execute("""

CREATE TABLE IF NOT EXISTS city (

City_Id INTEGER PRIMARY KEY,

City_Name TEXT,

Country_Id INTEGER

)

""")

# Player Table

cursor.execute("""

CREATE TABLE IF NOT EXISTS player (

Player_Id INTEGER PRIMARY KEY,

Player_Name TEXT

)

""")

# Season Table

cursor.execute("""

CREATE TABLE IF NOT EXISTS season (

Season_Id INTEGER PRIMARY KEY,

Man_of_the_Series INTEGER

)

""")

# Team Table

cursor.execute("""

CREATE TABLE IF NOT EXISTS team (

Team_Id INTEGER PRIMARY KEY,

Team_Name TEXT

)

""")

# ---------------- INSERT VALUES ----------------

# Country Data

cursor.execute("INSERT INTO country VALUES (1, 'India')")

cursor.execute("INSERT INTO country VALUES (2, 'England')")

# City Data

cursor.execute("INSERT INTO city VALUES (1, 'Delhi', 1)")

cursor.execute("INSERT INTO city VALUES (2, 'Mumbai', 1)")

cursor.execute("INSERT INTO city VALUES (3, 'London', 2)")

# Player Data

cursor.execute("INSERT INTO player VALUES (1, 'Virat')")

cursor.execute("INSERT INTO player VALUES (2, 'Rohit')")

cursor.execute("INSERT INTO player VALUES (3, 'Buttler')")

# Season Data

cursor.execute("INSERT INTO season VALUES (101, 1)")

cursor.execute("INSERT INTO season VALUES (102, 2)")

# Team Data

cursor.execute("INSERT INTO team VALUES (1, 'RCB')")

cursor.execute("INSERT INTO team VALUES (2, 'MI')")

cursor.execute("INSERT INTO team VALUES (3, 'RR')")

# Save Changes

conn.commit()

# ---------------- SHOW ALL TABLES ----------------

tables = pd.read_sql_query(

"""

SELECT name

FROM sqlite_master

WHERE type='table';

""",

conn,

)

print("\nALL TABLES:")

print(tables)

# ---------------- INNER JOIN ----------------

joined_city = pd.read_sql_query(

"""

SELECT c.Country_Id,

c.Country_Name,

ci.City_Name

FROM country c

INNER JOIN city ci

ON c.Country_Id = ci.Country_Id;

""",

conn,

)

print("\nINNER JOIN RESULT:")

print(joined_city)

# ---------------- LEFT JOIN ----------------

joined_left = pd.read_sql_query(

"""

SELECT *

FROM player p

LEFT JOIN season s

ON p.Player_Id = s.Man_of_the_Series;

""",

conn,

)

print("\nLEFT JOIN RESULT:")

print(joined_left)

# ---------------- CROSS JOIN ----------------

joined_cross = pd.read_sql_query(

"""

SELECT c.Country_Id,

c.Country_Name,

ci.City_Name

FROM country c

CROSS JOIN city ci;

""",

conn,

)

print("\nCROSS JOIN RESULT:")

print(joined_cross)

# ---------------- UNION ----------------

union_query = pd.read_sql_query(

"""

SELECT Player_Name AS Name

FROM player

UNION

SELECT Team_Name AS Name

FROM team;

""",

conn,

)

print("\nUNION RESULT:")

print(union_query)

# ---------------- CLOSE CONNECTION ----------------

conn.close()