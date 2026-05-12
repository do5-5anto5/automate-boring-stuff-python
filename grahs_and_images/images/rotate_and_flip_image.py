from PIL import Image

cat_pic = Image.open('gen_files/images/funny_cat.png')

cat_pic.rotate(90).save('gen_files/images/rotated90.png')
cat_pic.rotate(180).save('gen_files/images/rotated180.png')
cat_pic.rotate(270).save('gen_files/images/rotated270.png')

# optional expanding
cat_pic.rotate(6).save('gen_files/images/rotated6.png')
cat_pic.rotate(6, expand=True).save('gen_files/images/rotated6_expanded.png')

# mirror flip with transpose()

cat_pic.transpose(Image.FLIP_LEFT_RIGHT).save('gen_files/images/flipped_horizontal.png')
cat_pic.transpose(Image.FLIP_TOP_BOTTOM).save('gen_files/images/flipped_vertical.png')