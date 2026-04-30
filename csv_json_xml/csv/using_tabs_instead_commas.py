import csv

# Tab separated value files (TSV)
output_file = open('gen_files/output.tsv', 'w', newline='')
output_writer = csv.writer(output_file, delimiter='\t', lineterminator='\n\n')

output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])


output_file.close()