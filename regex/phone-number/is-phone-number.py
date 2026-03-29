import re

# #isPhoneNumber() function has code that does several checks to see
#
# whether the string in text is a valid phone number.


def is_phone_number(text: str) -> bool:
    if len(text) != 13:
        return False

    for i in range(0, 2):
        if not text[i].isdecimal():
            # print("non decimal 1")
            return False

    if text[2] != "-" or text[8] != "-":
        # print("no hifen")
        return False

    for i in range(3, 8):
        if not text[i].isdigit():
            # print("non decimal 2")
            return False

    for i in range(9, 13):
        if not text[i].isdecimal():
            # print("non decimal 3")
            return False

    return True

# find_phone_number goes through the entire string,
# testing each 12-character piece and printing any chunk it finds that satisfies
# isPhoneNumber().
def find_phone_number(message: str):
    for i in range(len(message)):
        chunk = message[i : i + 13]
        if is_phone_number(chunk):
            print(f'Phone number found: {chunk}')

message = (
    f"Please, call me at number 55-98140-0020 tomorrow. 55-33532-1234 is my office number"
)

find_phone_number(message)


