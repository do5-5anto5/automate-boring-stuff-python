import os, subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # soft deprecated


import subprocess # recomended simple to windows usage

def clear_with_subprocess():
        subprocess.run(['cls'], shell = True)