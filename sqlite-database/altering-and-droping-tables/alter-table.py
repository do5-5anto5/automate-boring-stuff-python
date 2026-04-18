import sqlite3

connection = sqlite3.connect("sweigartcats.db", isolation_level=None)

# get the table name >>> cats
print(
    connection.execute('SELECT name FROM sqlite_schema WHERE type = "table"').fetchall()
)
# alter cats table name to felines
connection.execute('ALTER TABLE cats RENAME TO felines')

# review table name >>> felines
print(
    connection.execute('SELECT name FROM sqlite_schema WHERE type = "table"').fetchall()
)

# get the second column name >>> fur
print(connection.execute('PRAGMA TABLE_INFO(felines)').fetchall()[2])

# alter column name to 'description'
connection.execute('ALTER TABLE felines RENAME COLUMN fur TO description')

# review the second column name >>> description
print(connection.execute('PRAGMA TABLE_INFO(felines)').fetchall()[2])

