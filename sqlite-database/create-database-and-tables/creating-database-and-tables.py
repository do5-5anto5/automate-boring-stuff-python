"""Connect to SQLite database 'first.db':
    the isolation_level=None keyword argument causes the database to use
    write-ahead logging, or WAL mode.

Create a table named 'cats' if it does not already exist.
The 'cats' table has three columns: 'name', 'birthdate', and 'weight_kg'. The 'name' column is a required TEXT type,
the 'birthdate' column is a TEXT type, and the 'weight_kg' column is a REAL type.
The table is created with the STRICT keyword, which means that SQLite will not silently ignore any data type mismatches. 
Instead, it will raise an error if such a mismatch occurs.
"""

import sqlite3

def create_connection():
    connection = sqlite3.connect('first.db', isolation_level=None)
    connection.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')

    print('Done.')

create_connection()
