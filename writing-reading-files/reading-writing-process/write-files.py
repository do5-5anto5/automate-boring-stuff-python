# open file with 'w' as second argument, to write the file from zero
# If the file already contains content, it will be overwritten
bacon_file = open("writing-reading-files\\files\\bacon.txt", "w")
bacon_file.write("Hello world!\n")

# after reading or writing a file, call the
# close() method before opening the file again
bacon_file.close()

# append mode, on the other hand, will append text to the end of the existing file
# Pass 'a' to the second argument
bacon_file = open("writing-reading-files\\files\\bacon.txt", "a")
bacon_file.write("Bacon is not a vegetable!")
bacon_file.close()

bacon_file = open("writing-reading-files\\files\\bacon.txt")
content = bacon_file.read()
print(content)


# if the file does not exists yet, both write and append will create a new one