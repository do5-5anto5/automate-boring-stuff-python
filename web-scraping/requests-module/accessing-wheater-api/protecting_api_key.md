# Protecting API Keys with python-dotenv

## Install

```bash
pip install python-dotenv
```

## File structure

```
project/
├── .env            # real keys — never commit
├── .env.example    # template without values — commit this
├── .gitignore
└── main.py
```

## .env
```
MY_API_KEY=yourkeyhere
```

## .env.example (show a .env structure to version/documentation without expose secrets)
```
MY_API_KEY=
```

## .gitignore
```
.env
```

## Code

```python
from dotenv import dotenv_values

config = dotenv_values('.env')
API_KEY = config.get('MY_API_KEY')
```

## Golden rule

Add `.env` to `.gitignore` **before** creating the file. New project, first commit already has `.gitignore` configured.
