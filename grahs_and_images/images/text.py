from PIL import Image, ImageDraw, ImageFont
import os 

img = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(img)
draw.text((20,150), 'Automate', fill='purple')
arial_font = ImageFont.truetype('arial.ttf', 32)
draw.text((100,150), 'Stuff', fill='gray', font=arial_font)
arial_font = ImageFont.truetype('arial.ttf', 32)

img.show()
img.save('gen_files/images/text.png')