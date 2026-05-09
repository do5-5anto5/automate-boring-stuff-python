from PIL import Image

cat_pic = Image.open('gen_files/images/funny_cat.png')
width, height = cat_pic.size

# resize() method returns a resized copy of this image.
quarter_sized_image = cat_pic.resize((int(width / 2), int(height / 2)))
svelte_image = cat_pic.resize((width, height + 300))


quarter_sized_image.save('gen_files/images/quarter_sized.png')
svelte_image.save('gen_files/images/svelte.png')
