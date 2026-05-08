"""
This file is has the first examples of Gmail API usages
Make sure you have enabled Gmail API and OAuth in Google Cloud, enable the credentials and protect it.
"""

import ezgmail

ezgmail.send("recipent@example.com", "title", "body")

# attach files to email message providing an extra list argument
ezgmail.send(
    "recipent@example.com",
    "title",
    "body",
    ["gen_files\\alarm.wav", "gen_files\\output.tsv"],
)

# supply the optional keyword arguments cc and bcc to send carbon copies and blind carbon copies
ezgmail.send(
    "recipent@example.com",
    "title",
    "body",
    cc="friend@example.com",
    bcc="otherfriend@example.com, someoneelse@example.com",
)

# checking which Gmail adress your project is configured for
email = ezgmail.EMAIL_ADDRESS
print(email)
