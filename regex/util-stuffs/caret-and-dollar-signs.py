import re

# You can also use the caret symbol (^) at the start of a regex to indicate that
# a match must occur at the beginning of the searched text. Likewise, you can
# put a dollar sign ($) at the end of the regex to indicate the string must end
# with this regex pattern. And you can use the ^ and $ together to indicate
# that the entire string must match the regex—that is, it’s not enough for a
# match to be made on some subset of the string. 

begins_with_hello = re.compile(r'^Hello')

mo = begins_with_hello.search('Hello, world!')
print(mo.group())

mo1 = begins_with_hello.search('She said "Hello!"')
print(mo1 == None)


ends_with_number = re.compile(r'(\d)?\d$')

mo2 = ends_with_number.search('Your number is 43')
print(mo2.group())

mo3 = ends_with_number.search('She had 2 dollars.')
print(mo3 == None)
