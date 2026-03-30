import re

# The dot character means “any single character except the newline,” and the
# star character means “zero or more of the preceding character.”

name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = name_regex.search("First Name: Al Last Name: Sweigart")

print(mo.group())
print(mo.group(1))
print(mo.group(2))

# The dot-star uses greedy mode: It will always try to match as much text as
# possible. To match any and all text in a nongreedy fashion, use the dot, star,
# and question mark (.*?). Like with curly brackets, the question mark tells
# Python to match in a nongreedy way.

greedy_regex = re.compile(r'<.*>')
mo1= greedy_regex.search('<To serve man> for a dinner>')
print(mo1.group())

# To match any and all text in a nongreedy fashion, use the dot, star,
# and question mark (.*?)

non_greedy_regex = re.compile(r'<.*?>')
mo2= non_greedy_regex.search('<To serve man> for a dinner>')
print(mo2.group())


# To match any and all text in a nongreedy fashion, use the dot, star,
# and question mark (.*?)

no_new_line_regex = re.compile(r'.*')
mo3 = no_new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo3.group())

new_line_regex = re.compile(r'.*', re.DOTALL)
mo4 = new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo4.group())
