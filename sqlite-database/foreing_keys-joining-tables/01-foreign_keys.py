"""
Complex data is best organized into multiple tables, which can be linked together using foreign keys.
This example uses to add vaccinations data to sweigartcats.db
"""

import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

# WARNING: The PRAGMA Foreign_keys = ON requires that the referenced column be explicitly declared.

# Implicit rowid referencing (REFERENCES table(rowid)) causes an OperationalError with the PRAGMA active.

# To use FK correctly, declare the parent table with INTEGER PRIMARY KEY:

#
# CREATE TABLE cats (id INTEGER PRIMARY KEY, name TEXT, ...) STRICT

# # INTEGER PRIMARY KEY does not create a new column -- it's an explicit alias for rowid.

# When inserting, pass NULL for id and the SQLite assigned to rowid is automatically:

## INSERT VALUES INTO cats (NULL, "Zophie", ...)
# -- id = 1, rowid = 1, are the same value

## The FK then refers to cats(id) instead of cats(rowid).
connection.execute('PRAGMA foreign_keys = ON')

connection.execute(
    'CREATE TABLE IF NOT EXISTS vaccinations (vaccine TEXT, date_administered TEXT, adminitered_by TEXT, cat_id INTEGER, FOREIGN KEY(cat_id) REFERENCES felines(rowid)) STRICT'
)

connection.execute(
    'INSERT INTO vaccinations VALUES ("rabies", "2023-06-06", "Dr. Echo", 1)'
)
connection.execute(
    'INSERT INTO vaccinations VALUES ("FelV", "2023-06-06", "Dr. Echo", 1)'
)

print(connection.execute('SELECT * FROM vaccinations').fetchall())

connection.execute('INSERT INTO vaccinations VALUES ("rabies", "2023-07-11", "Dr. Echo", 23)')

print(connection.execute('SELECT * FROM felines INNER JOIN vaccinations ON felines.rowid = vaccinations.cat_id').fetchall())
