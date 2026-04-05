# Virtual Environments

### This solution with virtual environments separate installations of Python that have their own set of installed third-party packages.

#### Create and add a scripts folder to evironment variable PATH

- press Start menu
  -> search Edit environment variables
  -> which should open the Environment Variables window.
  -> Select Path from the User variable list on the top of the screen
  -> add scripts folder path

#### To create a virtual environment, cd to your Scripts folder (previously added to PATH variables) and run python –m venv .venv
 example
 ```terminal
C:\Users\al\Scripts>python -m venv .venv
```

#### To use the virtual environment’s Python version, you must activate it.

example:
```terminal
C:\Users\al\Scripts>cd .venv\Scripts
C:\Users\al\Scripts\.venv\Scripts>activate.bat
```

#### Installing packages from PyPI

#### Always use `-m pip` instead of calling `pip` directly.

example:
```terminal
C:\Users\al>python -m pip install package_name
```

#### The `-m` flag ensures the `pip` that runs belongs to the exact Python interpreter you called.

#### Without it, pip may point to a different Python installation on the system, installing the package in the wrong place and causing import errors.

# Indispensable CLI Commands (Windows)

#### where

Search for files or directories that match a specific pattern or criteria.
Useful to confirm which Python (or any executable) the system is actually using.

```terminal
C:\> where python
```

#### python --version

Check the current Python version in use.

example:
```terminal
C:\> python --version
```

#### pip list

List all packages installed in the current environment.

```terminal
C:\> python -m pip list
```

#### pip show

Show details about a specific installed package (version, location, dependencies).

```terminal
C:\> python -m pip show package_name
```

#### deactivate

Exit the active virtual environment and return to the system Python.
Must be called from inside the active venv's Scripts folder.

```terminal
C:\Users\al\Scripts\.venv\Scripts> deactivate
```
