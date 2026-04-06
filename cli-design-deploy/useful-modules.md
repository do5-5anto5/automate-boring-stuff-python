# Pyperclip
#### Pyperclip allows to interact with the user's clipboard. With `pyperclip`, we can copy text to the clipboard using the `pyperclip.copy()` function and retrieve text from the clipboard using the `pyperclip.paste()` function. This enables us to implement features such as copying command output to the clipboard, pasting input from the clipboard, and more.

# Bext
#### Bext allows to enhance the user interface with ASCII art and console manipulation capabilities. With `bext`, we can create colorful and visually appealing output, as well as manipulate the console window size and position.
example in interactive terminal
```
>>> import bext
>>> bext.fg('red')
>>> print('This text is red.')
This text is red.
>>> bext.bg('blue')
>>> print('Red text on blue background is an ugly color scheme.')
Red text on blue background is an ugly color scheme.
>>> bext.fg('reset')
>>> bext.bg('reset')
>>> print('The text is normal again. Ah, much better.')
The text is normal again. Ah, much better.
```
### Bext useful commmands:
- bext.clear()  Clears the screen
- bext.width() and bext.height()  Returns the current width (in columns)
- and height (in rows) of the terminal window, respectively
- bext.hide() and bext.show()  Hides and shows the cursor, respectively
- bext.title(text)  Changes the title bar of the terminal window to the
- text string
- bext.goto(x, y)  Moves the cursor to column x and row y in the terminal, where 0, 0 is the top-left position
- bext.get_key()  Waits for the user to press any key and then returns a
- string describing the key

# Options to play audio
### Nava
####  It plays an audio file by calling the Nava module’s play() method
example:
```
from nava import play
play("hello.mp3")
```

### AudioPlayer
#### It offers more controle above the reproduction(play, pause, stop, loop, volume adjust)
example :
```
from audioplayer import AudioPlayer
AudioPlayer("hello.mp3").play(block=True)
```