import subprocess
import subprocess

with open('gen_files\\hello.txt', 'w') as file_obj:
    file_obj.write('Hello, world.')

subprocess.run(['start', 'gen_files\\hello.txt'], shell=True)