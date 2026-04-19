"""
Creating indexes speeds up searches.
But since indexes use a bit more storage, insert and update operations become slightly slower.
Ideal if you read more data than you insert/update. 
"""

import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

# creating indexes
connection.execute('CREATE INDEX IF NOT EXISTS idx_name ON cats (name)').fetchall()
connection.execute('CREATE INDEX IF NOT EXISTS idx_birthdate ON cats (birthdate)').fetchall()

# dropping indexes
connection.execute('DROP INDEX idx_name')

# get all indexes from cats table
indexes = connection.execute('SELECT name FROM sqlite_schema WHERE type = "index" AND tbl_name = "cats"').fetchall()

print(indexes)
