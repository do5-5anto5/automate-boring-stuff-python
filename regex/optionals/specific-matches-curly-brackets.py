import re

# The regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.

regex = re.compile(r"(Ha){3,5}")
mo = regex.search("HaHaHa")
mo1 = regex.search(
    "HaHaHaHaHa"
)  # This is a 'greedy method' because it will return always the biggest result
mo2 = regex.search("Ha")  # None

print(f"{mo.group()}\n{mo1.group()}\n{mo2 == None}")


# Python’s regular expressions are greedy by default, which means that in
# ambiguous situations they will match the longest string possible. 
# The nongreedy version of the curly brackets, which matches the shortest string possible, 
# has the closing curly bracket followed by a question mark.

regex_nongreedy = re.compile(r'(Ha){3,5}?')
mo_nongreedy = regex_nongreedy.search('HaHaHaHaHa')

print(mo_nongreedy.group())