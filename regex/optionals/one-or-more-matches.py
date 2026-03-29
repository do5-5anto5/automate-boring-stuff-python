import re

regex = re.compile(r'Bat(wo)+man')

mo = regex.search('Batwowowowowoman')

print(mo.group())
print(mo.group(1))

mo2 = regex.search('Batman')
print(mo2 == None)