import ezgmail

# full list of search operators at https://support.google.com/mail/answer/7190

result_threads= ezgmail.search('Google')

print(ezgmail.summary(result_threads))