import os, subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # soft deprecated


import subprocess # recomended

def clear_with_subprocess():
        subprocess.run(['cls'], shell = True)