import csv

with open("gen_files\\examples3.csv") as example_file:
    reader = csv.reader(example_file)
    example_data = list(reader)

# now having the data as a list of lists, access the value at a particular row and column
print (example_data[0][0])
print (example_data[0][1])
print (example_data[0][2])
print (example_data[1][1])
print (example_data[6][1])