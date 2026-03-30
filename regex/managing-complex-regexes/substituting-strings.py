import re

# Regular expressions can not only find text patterns but can also substitute
# new text in place of those patterns. The sub() method for Regex objects is
# passed two arguments. The first argument is a string to replace any matches.
# The second is the string for the regular expression. The sub() method returns
# a string with the substitutions applied.

agent = re.compile(r'Agent \w+')
censored = agent.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(censored)

# Sometimes you may need to use the matched text itself as part of the
# substitution. In the first argument to sub(), you can type \1, \2, \3, and so
# on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
# For example, say you want to censor the names of the secret agents by
# showing just the first letters of their names. To do this, you could use the
# regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1
# in that string will be replaced by whatever text was matched by group 1—
# that is, the (\w) group of the regular expression.

names_regex = re.compile(r'Agent (\w)\w*')
secret_message = names_regex.sub(r'\1****', 'Agent Alice said to Agent Carol that Agent Eve knows about Agent Bob to be a double ')
print(secret_message)