import sqlite3

connection = sqlite3.connect('sweigartcats.db', isolation_level=None)
conn_backup = sqlite3.connect('backup.db', isolation_level=None)

connection.backup(conn_backup)
