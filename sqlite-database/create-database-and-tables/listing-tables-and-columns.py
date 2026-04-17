import sqlite3

def get_cats():
    connection = sqlite3.connect('first.db', isolation_level=None)

    # Get cats table from database
    cats = connection.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
    print(cats)

    # Get cats table columns info    
    cats_info = connection.execute('PRAGMA TABLE_INFO(cats)').fetchall()

    print(cats_info)
    # [(0, 'name', 'TEXT', 1, None, 0), (1, 'birthdate', 'TEXT', 0, None, 0), (2, 'fur', 'TEXT', 0, None, 0), (3, 'weight_kg', 'REAL', 0, None, 0)]
    
    # what is the meaning of each column
    # [@column_position, @column_name, @data_type, @is_nullable, @default_value, @primary_key]


get_cats()