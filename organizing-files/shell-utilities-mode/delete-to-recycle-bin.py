# install third party Send 2 Trash at project
# at terminal: pip install send2trash
import send2trash


# send2trash module’s send2trash() function send folders and files to
# computer’s trash or recycling bin instead of permanently deleting them,
# allowing file recover
send2trash.send2trash('bacon.txt')