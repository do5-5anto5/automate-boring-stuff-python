import ezgmail

unread_threads = ezgmail.unread()
ezgmail.summary(unread_threads)

# printint a spefic email details
print(f'''unread threads list length: {len(unread_threads)}
{unread_threads[0]}
{len(unread_threads[0].messages)}
{unread_threads[0].messages[0]}
{unread_threads[0].messages[0].subject}
{unread_threads[0].messages[0].body}
{unread_threads[0].messages[0].timestamp}
{unread_threads[0].messages[0].sender}
{unread_threads[0].messages[0].recipient}
''')

# get recent emails
recent_threads = ezgmail.recent()
print(f'recents len: {len(recent_threads)}')
# getting more than 25 default quantity
recent_threads = ezgmail.recent(maxResults=100)
print(f'recents len: {len(recent_threads)}')

