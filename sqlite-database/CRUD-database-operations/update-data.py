import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

# check current Zophie data
zophie = connection.execute('SELECT * FROM cats WHERE rowid = 1').fetchall()

print(zophie)

# update Zophie data
connection.execute('UPDATE cats SET fur = "gray tabby" WHERE rowid = 1')

# check updated data
zophie_update = connection.execute('SELECT * FROM cats WHERE rowid = 1').fetchall()
print(zophie_update)

