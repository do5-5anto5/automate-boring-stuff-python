import sqlite3

connection = sqlite3.connect('first.db', isolation_level=None)

# get a list from full table objects
cats = connection.execute('SELECT * FROM cats').fetchall() 
print(cats)

# get just the rowid and name columns from table cats
rowid_names = connection.execute('SELECT rowid, name FROM cats').fetchall()
print(rowid_names)