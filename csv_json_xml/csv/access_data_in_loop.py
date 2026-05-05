import csv

with open('gen_files\\examples3.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f'Row #{reader.line_num} {row}')