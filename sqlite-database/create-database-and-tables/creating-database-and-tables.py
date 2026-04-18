"""Connect to SQLite database 'first.db':
    the isolation_level=None keyword argument causes the database to use
    write-ahead logging, or WAL mode.

Create a table named 'cats' if it does not already exist.
The 'cats' table has three columns: 'name', 'birthdate', and 'weight_kg'. The 'name' column is a required TEXT type,
the 'birthdate' column is a TEXT type, and the 'weight_kg' column is a REAL type.

NOTE: No 'id' column is declared here, so the table relies on SQLite's implicit
rowid. This works for basic queries (SELECT rowid, ...) but will cause an
OperationalError if PRAGMA foreign_keys = ON is active and another table tries
to reference this table via a foreign key.
To support foreign keys, declare an explicit primary key instead:
    cats (id INTEGER PRIMARY KEY, name TEXT NOT NULL, ...)
INTEGER PRIMARY KEY is not a new column -- it is a named alias for the rowid,
assigned automatically when NULL is passed on insert.

The STRICT keyword prevents silent type coercion: SQLite will raise an error
on any type mismatch instead of converting the value silently.
"""

import sqlite3

def create_connection():
    connection = sqlite3.connect('first.db', isolation_level=None)
    connection.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')
                        # CREATE TABLE cats (id INTEGER PRIMARY KEY, name TEXT, ...) STRICT 

    print('Done.')

create_connection()
