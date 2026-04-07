# Deploying Python programs in Windows
#### - Place your script file scriptfilename.py  in Scripts folder (previously added to Environment Variables).
#### - Create a scriptfilename.bat in this folder to run the Python script 
.bat file defaul content:
```
@call %HOMEDRIVE%%HOMEPATH%\Scripts\.venv\Scripts\activate.bat
@python %HOMEDRIVE%%HOMEPATH%\Scripts\yourScript.py %*
@pause
@deactivate
```
#### %HOMEDRIVE%%HOMEPATH% points to a default directory, which would be C:/username/
#### It is useful when you share the script. 

.bat file content
```
@call D:\customfoldername\Scripts\.venv\Scripts\activate.bat
@python D:\customfoldername\Scripts\snowstorm.py %*
@pause
@deactivate
```