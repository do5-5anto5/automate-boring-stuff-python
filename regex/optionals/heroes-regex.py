import re

# match any of the strings 'Batman',
# 'Batmobile', 'Batcopter', and 'Batbat'. Since all these strings start with Bat.
# This can be done with parentheses and pipes.
rgx = re.compile(r"Bat(man|mobile|bat)")

mo = rgx.search("Batmobile lost a wheel")

print(mo.group(0))
print(mo.group(1))
print()

# the regex should find a match whether or not that bit of text is there.
# The ? character flags the group that precedes it as an optional part of the
# pattern.

rgx_wo = re.compile(r"Bat(wo)?man")

mo1 = rgx_wo.search("The adventures of Batwoman")
print(mo1.group())
mo2 = rgx_wo.search("The adventures of Batman")
print(mo2.group())
print()

# The * (called the star or asterisk) means “match zero or more”—the group
# that precedes the star can occur any number of times in the text

rgx_wowowo = re.compile(r'Bat(wo)*man')
mo3 = rgx_wowowo.search('The adventures of Batwowowowowowoman!')

print(mo3.group())