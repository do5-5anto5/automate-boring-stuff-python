# reading a file
hello_file = open('writing-reading-files\\files\\hello.txt')
hello_content = hello_file.read()
print(hello_content)

# use the readlines() method to get a list of string
# values from the file, one string for each line of text
sonnet_file = open('writing-reading-files\\files\\sonnet29.txt')
print(sonnet_file.readlines())
