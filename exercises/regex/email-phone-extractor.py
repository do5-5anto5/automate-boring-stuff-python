import re
from data import data

phone_regex = re.compile(
    r"""(
(\d{2}|\(\d{2}\))?           # area code
(\s|-|\.)?                   # separator
\d{5}                        # first 5 digits
(\s|-|\.)                    # separator
\d{4}                        # last 4 digits
)""",
    re.VERBOSE,
)

# email_regex = re.compile(
#     r"""\w+
# (\.)?(\w+)?(\.)?(\w+)?
# @\w+
# (\.)?(\w+)?(\.)?(\w+)?\.\w+""",
#     re.VERBOSE,
# )

# email_regex = (re.compile(r'Email: (.*)'))

email_regex = re.compile(r'[\w\.]+@[\w\.]+\.\w+')

email = email_regex.search("Nome: Henrique Pinto, Profissão: Desenvolvedor, Email: henriquepinto@hotmail.com, Telefone: 81-99267-5749")
emails = email_regex.findall(data)

# print(email.group())
# print(emails)

phones = phone_regex.findall(data)
phones2 = [match[0] for match in phone_regex.findall(data)]

print(phones2)
