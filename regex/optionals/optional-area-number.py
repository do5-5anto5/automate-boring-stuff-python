import re

phone_regex= re.compile(r'(\d\d-)?\d\d\d\d\d-\d\d\d\d')             

mo = phone_regex.search('My phone number is 33531-7500')
mo1 = phone_regex.search('My phone number is 71-33531-7500')

print(mo.group())
print(mo1.group())

