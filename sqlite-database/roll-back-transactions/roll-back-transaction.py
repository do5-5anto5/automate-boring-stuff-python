"""
As default, queries run and finish every time calling connection.execute() when in WAL mode (isolation_level=None).

Running BEGIN query you can finish it calling connection.commit()
or undo it calling connextion.rollback() .

This example adds two cats to database, then roll back the query
"""

import sqlite3

def insert_fluffy_and_socks(conn):
    conn.execute('INSERT INTO cats VALUES("Socks", "2022-04-04", "white", 4.2)')
    conn.execute('INSERT INTO cats VALUES("Fluffy", "2022-04-04", "gray", 4.5)')

def print_fluffy_and_socks_data(conn):
    socks = conn.execute('SELECT * FROM cats WHERE name = "Socks"').fetchall()
    fluffy = conn.execute('SELECT * FROM cats WHERE name = "Fluffy"').fetchall()
    print(socks)
    print(fluffy)


connection = sqlite3.connect('sweigartcats.db', isolation_level=None)

connection.execute('BEGIN')

insert_fluffy_and_socks(connection)

# rolling back query
connection.rollback()

print_fluffy_and_socks_data(connection)

# redoing the command insertion
insert_fluffy_and_socks(connection)

# commiting query
connection.commit()

print_fluffy_and_socks_data(connection)
