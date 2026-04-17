import sqlite3
from pprint import pprint

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

# sort by fur
fur_list = connection.execute('SELECT * FROM cats ORDER BY fur').fetchall()
pprint(fur_list)

print()

# sort by fur, then by birthdate, choose ascending or descending order
fur_birthdate = connection.execute('SELECT * FROM cats ORDER BY fur ASC, birthdate DESC').fetchall()
pprint(fur_birthdate)
