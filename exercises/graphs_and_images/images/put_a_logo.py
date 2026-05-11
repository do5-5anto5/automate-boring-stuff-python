import os
from PIL import Image

IMAGES = f'gen_files/images/'
FIT_SIZE = 300
LOGO_FILENAME = 'gen_files/images/catlogo.png'

logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

# check / create destination path
os.makedirs(f'{IMAGES}/with_logo', exist_ok=True)


for filename in os.listdir(IMAGES):
    if (
        not filename.endswith('.png')
        or filename.endswith('.jpg')
        or filename == LOGO_FILENAME
    ):
        continue

    img = Image.open(f'{IMAGES}/{filename}')
    width, height = img.size    

    # business rule for resizing
    if width > FIT_SIZE and height > FIT_SIZE:
        if width > height:
            height = int((FIT_SIZE / width) * height)
            width = FIT_SIZE
        else:
            width = int((FIT_SIZE / height) * width)
            height = FIT_SIZE

        print(f'Resizing {filename}')
        img = img.resize((width, height))

        img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

        img.save(os.path.join(f'{IMAGES}/pewith_logo', filename))
