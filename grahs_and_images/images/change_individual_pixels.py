from PIL import Image, ImageColor

# create image
img = Image.new('RGBA', (100, 100))

# print checking pixel 0,0 color value
print(img.getpixel((0, 0)))


# change pixels, colouring them
for x in range(100):
    for y in range(50):
        img.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        img.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

# print checking pixels changed
print(f"""
{img.getpixel((0,0))}
{img.getpixel((0,50))}
""")

# show and save image
img.show()
img.save("gen_files/images/ind_pxl.png")