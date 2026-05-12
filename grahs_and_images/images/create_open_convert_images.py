from email.mime import image

from PIL import Image

# create images
# create a width:100 x height:200 image with purple backgroud, then save it
im = Image.new('RGBA', (100, 200), 'purple')
im.save('gen_files/images/purpleImage.png')
# create a 20x20 square image without backgroud, then save it
im2 = Image.new('RGBA', (20, 20))
im2.save('gen_files/images/transparentImage.png')


# ______________________________________

# get an image
cat_pic = Image.open('gen_files/images/funny_cat.png')

# open the image in a dedicated software
cat_pic.show()

# working with the image data type

width, height = cat_pic.size
print(width)
print(height)

filename = cat_pic.filename
img_format = cat_pic.format
fmt_descr = cat_pic.format_description

# save image converting it's format
cat_pic.save('gen_files/images/funny_cat.jpg')
