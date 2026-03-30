import re

# This is a phone number regex that find the numbers, independent of the separator used
phoneRegex = re.compile(
    r"((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)"
)

# Telling the re.compile() function
# to ignore whitespace and comments inside the regular expression string, usin re.VERBOSE.
# you can spread the regular expression over multiple lines with comments
# like this:

phoneRegex = re.compile(
    r"""(
(\d{3}|\(\d{3}\))?           # area code
(\s|-|\.)?                   # separator
\d{3}                        # first 3 digits
(\s|-|\.)                    # separator
\d{4}                        # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)""",
    re.VERBOSE,
)
