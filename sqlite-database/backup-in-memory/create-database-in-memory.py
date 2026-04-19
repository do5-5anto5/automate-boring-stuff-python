"""
For many queries, use an in-memory database: it's much faster, but the data will be lost if the program crashes.
Remember to use `backup()` to save the files.
"""

import sqlite3

memory_db_conn = sqlite3.connect(':memory:', isolation_level=None)

memory_db_conn.execute('CREATE TABLE test (name TEXT, numer REAL)')

memory_db_conn.execute('INSERT INTO test VALUES ("pi", 3.14)')

file_db_conn = sqlite3.connect('test.db', isolation_level=None)

memory_db_conn.backup(file_db_conn) # save the database to test.db