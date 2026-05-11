from PIL import Image
import pyperclipimg

img = Image.open('gen_files/images/funny_cat.jpg')
pyperclipimg.copy(img)

pasted_img = pyperclipimg.paste()
pasted_img.show()