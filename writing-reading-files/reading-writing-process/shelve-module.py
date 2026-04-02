import shelve

# save variables in your Python programs to binary shelf files using
# the shelve module

shelf_file = shelve.open("writing-reading-files\\files\\mydata")

cats = ["Sofia", "Tom", "Pooka"]
shelf_file["cats"] = cats

shelf_file.close()

# reading a shelf file, listing keys and values
shelf_file = shelve.open("writing-reading-files\\files\\mydata")
print(shelf_file["cats"])

shelf_file_keys = list(shelf_file.keys())
print(shelf_file_keys)

shelf_file_values = list(shelf_file.values())
print(shelf_file_values)
