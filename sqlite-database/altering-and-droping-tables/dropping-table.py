import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)
# mocking db to secure dropping show case
mock_conn = sqlite3.connect('mock_db.db', isolation_level=None)

connection.backup(mock_conn)

print(mock_conn.execute('SELECT * FROM sqlite_schema WHERE type = "table"').fetchall())

# this one command drops a table
mock_conn.execute('DROP TABLE felines')

print(mock_conn.execute('SELECT * FROM sqlite_schema WHERE type = "table"').fetchall())
