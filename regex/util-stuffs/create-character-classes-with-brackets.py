import re

vowel_regex = re.compile(r'[aeiouAEIOU]')
mo = vowel_regex.findall('Robocop eats baby food. BABY FOOD.')

print(mo)

# By placing a caret character (^) just after the character class’s opening
# bracket, you can make a negative character class. A negative character class
# will match all the characters that are not in the character class.

consonant_regex = re.compile(r'[^aeiouAEIOU]')

mo1 = consonant_regex.findall('Robocop eats baby food. BABY FOOD.')

print(mo1)