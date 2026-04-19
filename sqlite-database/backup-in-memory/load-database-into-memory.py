"""
The risk with in-memory databases is data loss in case of failure.
To avoid this, use try/except to save the database before the program terminates.
"""

import sqlite3

# load database original file
file_db_conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

# do the backup to memory
memory_db_conn = sqlite3.connect(':memory:', isolation_level=None)
file_db_conn.backup(memory_db_conn)

# close the database original file
file_db_conn.close()


try:
    # do anything in memory db connection
    pass
except Exception as e:
    backup_conn = sqlite3.connect('backup.db', isolation_level=None)
    memory_db_conn.backup(backup_conn)
    backup_conn.close()
    print('Failure - database saved to backup.db')
    print(e)
else:
    # only saves to the original file if there were no exceptions
    file_db_conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
    memory_db_conn.backup(file_db_conn)
    file_db_conn.close()