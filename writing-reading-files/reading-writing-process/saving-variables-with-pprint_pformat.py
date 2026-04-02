import pprint

cats = [{"name": "Tom", "desc": "chubby"}, {"name": "Frajola", "desc": "fluffy"}]

file_obj = open("writing-reading-files\\files\\my-cats.py", "w")
file_obj.write(pprint.pformat(cats))
file_obj.close()
