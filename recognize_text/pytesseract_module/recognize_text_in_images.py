import pytesseract as tess
from PIL import Image

img = Image.open('gen_files/images/ocr-example.png')
text = tess.image_to_string(img)
print(text)
img.close()

# text like next come with some errors, consider to use any logic (harder) to fix it
# or ask/integrate any llm model to fix the string
frank_img_text = Image.open('gen_files/images/frank_br.png')
text2 = tess.image_to_string(frank_img_text)
print(text2)

# recognizing text in non english language
print(tess.get_languages())
text3 = tess.image_to_string(frank_img_text, lang='por')
print(text3)