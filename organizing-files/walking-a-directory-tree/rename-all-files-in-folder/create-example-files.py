from pathlib import Path

current_path = Path(__file__).parent

# creating example files
(current_path / 'files').mkdir(exist_ok=True)
(current_path / 'files/grapes').mkdir(exist_ok=True)
(current_path / 'files/apples').mkdir(exist_ok=True)
(current_path / 'files/grapes/green').mkdir(exist_ok=True)

for f in ['files/file1.txt','files/grapes/file2.txt', 'files/apples/file3.txt', 'files/grapes/green/file4.txt']:
    with open(current_path / f , 'w', encoding='utf-8') as file:
        file.write('Hello')