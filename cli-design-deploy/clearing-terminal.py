import os, subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # soft deprecated


import subprocess # recomended

def clear_with_subprocess():
    """
    Clears the terminal using subprocess module.

    This function is more reliable than using os.system() as it does not
    rely on the shell being available.

    If the system is Windows (os.name == 'nt'), it runs 'cmd /c cls'
    to clear the terminal.

    If the system is not Windows, it runs 'clear' to clear the terminal.
    """
    if os.name == 'nt':
        subprocess.run(['cmd', '/c', 'cls'])
    else:
        subprocess.run(['clear'])