import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

three_cats = connection.execute('SELECT * FROM cats LIMIT 3').fetchall()

print(three_cats)

# dont use 
#       >>> connection.execute('SELECT * FROM cats LIMIT 3').fetchall()[:3]
# it is inneficient.
# it fetches all the rows before, and discards all other elements except first 3