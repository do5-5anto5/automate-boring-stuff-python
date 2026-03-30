import re

# To make your regex case-insensitive, 
# you can pass re.IGNORECASE or re.I as a second argument to re.compile()

case_insensitive_regex = re.compile(r'robocop', re.I)
mo1 = case_insensitive_regex.search('RoboCop is a part machine, part man, all cop.')
mo2 = case_insensitive_regex.search('ROBOCOP protects the innocents')
mo3 = case_insensitive_regex.search('Jonathan, why does your programming exercises talk about robocop so much?')

print(f'{mo1.group()}\n{mo2.group()}\n{mo3.group()}')
