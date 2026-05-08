import ezgmail

threads = ezgmail.search('title')

# download a spefic attachment
threads[0].messages[0].downloadAttachment('alarm.wav')

# download all attachments, define a destination folder
threads[0].messages[0].downloadAllAttachments(downloadFolder='gen_files\\attachments')
ezgmail.summary(threads)