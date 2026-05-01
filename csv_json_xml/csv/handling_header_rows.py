import csv, pprint
 
# reading a CSV file with header row
example_file = open('gen_files\\exampleWithHeader3.csv')
dict_reader = csv.DictReader(example_file)
example_dict_data = list(dict_reader)

pprint.pprint(example_dict_data)
example_file.close()

# writing a CSV with a header row

output_file = open('gen_files/output_with_header.csv', 'w', newline='')
outuput_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
outuput_dict_writer.writeheader() # write header row with writeheader()

outuput_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-4321'})
outuput_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-8888'})
outuput_dict_writer.writerow({'Phone': '555-4444', 'Name': 'Carol', 'Pet': 'dog', })

output_file.close()

