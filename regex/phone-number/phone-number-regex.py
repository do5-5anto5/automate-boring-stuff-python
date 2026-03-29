import re

message = f"Please, call me at number 55-98140-0020 tomorrow. 55-33532-1234 is my office number"

# using Regex, solve it with 2 lines, instead of writing nested loops and conditions

phone_num_regex = re.compile(r"\d\d-\d\d\d\d\d-\d\d\d\d")
# find just the first occurency
match_object = phone_num_regex.search(message)

print(f"phone found: {match_object.group()}")


# find all occurencies, return a list with them
print(phone_num_regex.findall(message))


#########


# more pattern matches

# separates subgroups

s_phone_num_regex = re.compile(r"(\d\d)-(\d\d\d\d\d-\d\d\d\d)")
s_match_object= s_phone_num_regex.search(message)

#first occurency
print(f'phone found: {s_match_object.group(0)} \nprefix: {s_match_object.group(1)} \nnumber: {s_match_object.group(2)}')

# all occurencies
phones = s_phone_num_regex.findall(message)

for prefix, number in phones:
    print(f'prefix: {prefix} number: {number}')