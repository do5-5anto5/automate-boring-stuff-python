"""
SQLite database demonstration script for managing people and addresses.

This module creates and populates a SQLite database with three related tables:
- pessoa: stores basic person information
- pessoa_x_endereco: relationship table between people and addresses
- endereco: stores complete address data

The script demonstrates:
- Creating tables with relationships and foreign keys
- Inserting sample data
- JOIN queries to combine person and address information

The database is saved as 'db_zada.db' in the same directory as the script.
"""

import sqlite3, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "db_zada.db")

connection = sqlite3.connect(DB_PATH, isolation_level=None)

connection.execute(
    """
    CREATE TABLE IF NOT EXISTS pessoa (
       id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento TEXT
    ) STRICT
"""
)

connection.execute(
    """
    CREATE TABLE IF NOT EXISTS endereco (
        cep TEXT PRIMARY KEY,
        logradouro TEXT,
        bairro TEXT,
        cidade TEXT,
        uf TEXT
    ) STRICT
"""
)

connection.execute(
    """
    CREATE TABLE IF NOT EXISTS pessoa_x_endereco (
        id_pessoa INTEGER,
        cep TEXT,
        numero INTEGER,
        complemento TEXT,
        PRIMARY KEY (id_pessoa, cep),
        FOREIGN KEY(id_pessoa) REFERENCES pessoa(id)
        FOREIGN KEY(cep) REFERENCES enderco(cep)
    ) STRICT
"""
)


connection.execute('INSERT OR IGNORE INTO pessoa VALUES (NULL, "Allcs", "01/01/1900")')
connection.execute('INSERT OR IGNORE INTO pessoa_x_endereco VALUES (1, "000-0000", 100, NULL)')
connection.execute(
    'INSERT OR IGNORE INTO endereco VALUES ("000-0000", "rua", "bairro", "cidade", "MG")'
)


pessoas = connection.execute(
    """
    SELECT
        p.nome,
        e.logradouro,
        px.numero,
        px.complemento,
        e.bairro,
        e.cidade,
        e.uf
    FROM pessoa p JOIN pessoa_x_endereco px ON p.id = px.id_pessoa
    JOIN endereco e ON px.cep = e.cep
"""
).fetchall()

for row in pessoas:
    print(row)
