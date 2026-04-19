# SQLite Apps — Chapter Notes

## SQLite3 CLI Installation (Windows)

1. Download `sqlite-tools-win-x64-*.zip` from https://sqlite.org/download.html  
   — Under **Precompiled Binaries for Windows**, pick the `sqlite-tools` option (not the DLL).  
   — The DLL packages are for developers linking SQLite into other programs. The tools package includes `sqlite3.exe`, which is the command-line shell.

2. Extract to any folder on any drive (e.g. `D:\sqlite`).

3. Add that folder to the Windows `PATH`:  
   Control Panel → System → Advanced system settings → Environment Variables → `Path` → New → paste the folder path.

4. Open a new terminal and verify:
   ```
   sqlite3 --version
   ```

---

## Why Use the CLI

The CLI is useful for quick inspection and testing: it displays query results as a formatted table, giving immediate visual feedback without running a Python script. It is **not** a replacement for writing table definitions in source code.

- **CLI**: test queries, inspect data, explore structure quickly.
- **Source code**: create tables, define foreign keys, implement business logic. This keeps the schema versioned, commented, and reproducible across machines.

---

## CLI Session Example

```
sqlite3 example.db

sqlite> CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT;
sqlite> .tables
cats
sqlite> INSERT INTO cats VALUES ('Zophie', '2021-01-27', 'gray tabby', 4.7);
sqlite> SELECT * FROM cats;
```

| name   | birthdate  | fur        | weight_kg |
|--------|------------|------------|-----------|
| Zophie | 2021-01-27 | gray tabby | 4.7       |

---

## GUI Alternative

If you want a more fully-featured interface with a visual schema browser, query editor, and data editor, see:
• DB Browser for SQLite (https://sqlitebrowser.org)
• SQLite Studio (https://sqlitestudio.pl)
• DBeaver Community (https://dbeaver.io)