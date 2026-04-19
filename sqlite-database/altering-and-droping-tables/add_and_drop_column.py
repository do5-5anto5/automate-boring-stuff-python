import sqlite3, pprint

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

# adding is_loved column
connection.execute('ALTER TABLE felines ADD COLUMN is_loved INTEGER DEFAULT 1')

pprint.pprint(connection.execute('PRAGMA TABLE_INFO(felines)').fetchall())
pprint.pprint(connection.execute('SELECT * FROM felines LIMIT 3').fetchall())

# dropping is_loved column
connection.execute('ALTER TABLE felines DROP COLUMN is_loved' '')

pprint.pprint(connection.execute('PRAGMA TABLE_INFO(felines)').fetchall())
pprint.pprint(connection.execute('SELECT * FROM felines LIMIT 3').fetchall())
