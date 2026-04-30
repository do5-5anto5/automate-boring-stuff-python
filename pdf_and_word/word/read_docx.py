import docx

def get_text(filename: str) -> str:
    doc = docx.Document(filename)
    full_text = []

    for p in doc.paragraphs:
        full_text.append(p.text)

    return '\n'.join(full_text)

text = get_text('D:\\DevTools\\web\\code\\automate-boring-stuff-python\\gen_files\\demo.docx')

print(text)