from PIL import Image

cat_pic = Image.open('gen_files/images/funny_cat.png')

# Paste image onto other image at specific coordinates
cat_pic_copy = cat_pic.copy()
eyes_pic = Image.open('gen_files/images/cropped.png')
print(eyes_pic.size)
cat_pic_copy.paste(eyes_pic, (0,0))
cat_pic_copy.paste(eyes_pic, (900,365))
cat_pic_copy.save('gen_files/images/pasted.png')


#____________________________________________________

# Loop pasting image - 'grid effect'
cat_pic_width, cat_pic_height = cat_pic.size
eyes_pic_width, eyes_pic_height = eyes_pic.size
cat_pic_grid_copy = cat_pic.copy()

for left in range(0, cat_pic_width, eyes_pic_width):
    for top in range(0, cat_pic_height, eyes_pic_height):
        print(left, top)
        cat_pic_grid_copy.paste(eyes_pic, (left, top))
cat_pic_grid_copy.save('gen_files/images/cat_grid_pasted.png')