from PIL import Image

cat_pic = Image.open('gen_files/images/funny_cat.png')

# Croping image

# crop() method Returns a rectangular region from this image.
# The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate. See coordinate-system
# Note: crop() creates the new file from the original
cropped_pic = cat_pic.crop((360, 650, 1460, 1445))
cropped_pic.save('gen_files/images/cropped.png')
