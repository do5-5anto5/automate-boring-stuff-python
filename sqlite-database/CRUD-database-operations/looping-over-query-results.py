import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

for row in connection.execute('SELECT * FROM cats'):
    print('Row data:', row)
    print(row[0], 'is of my favorite cats')