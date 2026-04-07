### You'll need to install the module PyInstaller
on terminal:
```
python -m install PyInstaller
```

### Then run build command
on terminal:
```
python -m PyInstaller --onefile yourscript.py
```

#### This will create a build folder (can be deleted) and a dist folder, wich will contain the executable.
#### It is really useful to share the script with person who might not have Python installed