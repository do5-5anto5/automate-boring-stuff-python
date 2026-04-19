import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

# check first position at cats table
first_cat_data = connection.execute('SELECT * FROM cats WHERE rowid = 1').fetchall()
print(first_cat_data)

# delete
connection.execute('DELETE FROM cats WHERE rowid = 1')

first_cat_data = connection.execute('SELECT * FROM cats WHERE rowid = 1').fetchall()
print(first_cat_data) # empty
