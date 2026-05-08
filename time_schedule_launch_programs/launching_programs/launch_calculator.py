import subprocess, time
import psutil # (process and system utilities) https://pypi.org/project/psutil/

subprocess.run('calc')
time.sleep(3)

for proc in psutil.process_iter(['name']):
    if 'calculator' in proc.info['name'].lower():
        proc.kill()


# In previous versions of Windows, `subprocess.run` with GUI apps would freeze the terminal until the window was closed.
# In Windows 11, the default behavior is to return immediately 
# — use Popen if you need to launch without blocking.

# Legacy code, about Windows 10
# calc_proc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
# print(calc_proc.poll == None)
# print(calc_proc.wait())
# calc_proc.kill()
