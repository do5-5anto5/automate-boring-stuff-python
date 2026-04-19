import sqlite3

# Stabilish database connection
connection = sqlite3.connect('first.db', isolation_level=None)

# Insert Zophie into database


name = 'Zophie'
birthday = '2021-01-24'
fur= 'black'
wheigth= 5.6
connection.execute(f'INSERT INTO cats VALUES("{name}", "{birthday}", "{fur}", {wheigth})')

# connection.execute('INSERT INTO cats VALUES("Zophie", "2021-01-04", "black", 5.6)')
# This line is intended for study purposes. However, it is vulnerable to SQL injection. For example, someone with malicious intent could, through knowledge, change this string and do things your system doesn't want done to the database.
# It is recommended to use question marks (?) and variables. to prevent it
