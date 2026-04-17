"""
Operators to filter
=, !=, <, >, <=, >=, AND, OR, NOT

% - wildcard case insensitive
* - wildcard case sensitive
"""

import sqlite3, pprint

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

# match all black cats
black_cats = connection.execute('SELECT * FROM cats WHERE fur = "black"').fetchall()
print(black_cats)

# match names that ends "y" - LIKE "%y"
names_ends_y = connection.execute('SELECT rowid, name FROM cats WHERE name LIKE "%y"').fetchall()
print(names_ends_y)

# match names that starts "Ja" - LIKE "Ja%"
names_starts_ja = connection.execute('SELECT rowid, name FROM cats WHERE name LIKE "Ja%"').fetchall()
print(names_starts_ja)

# match names that has 'ob' anywhere in them (case insensitive) - LIKE "%str%" 
names_ob_anywhere = connection.execute('SELECT rowid, name FROM cats WHERE name LIKE "%ob%"').fetchall()
print(names_ob_anywhere)

# match names that has 'ob' anywhere in them (case sensitive) - GLOB "*str*"
names_m_nwhr_sns = connection.execute('SELECT rowid, name FROM cats WHERE name GLOB "*m*"').fetchall()
print(names_m_nwhr_sns)

# pretty printing retrieved list
matching_cats = connection.execute('SELECT * FROM cats WHERE fur = "black" OR birthdate >= "2024-01-01"').fetchall()
pprint.pprint(matching_cats)