import pyperclip, time

previous_content =  pyperclip.paste()

try:
    while True:
        content = pyperclip.paste()
        if content != previous_content:
            print(content)
            previous_content = content
        
        time.sleep(0.01)
except KeyboardInterrupt:
    pass


print('Press CTRL + C to stop.')