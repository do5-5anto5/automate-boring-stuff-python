import re

# The . (or dot) character in a regular expression is called a wildcard and will
# match any character except for a newline. 

at_regex = re.compile(r'.at')
mo = at_regex.findall('The cat in the hat sat on the flat mat.')
print(mo)