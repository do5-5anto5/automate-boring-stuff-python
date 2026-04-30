import docx

doc = docx.Document("gen_files/demo.docx")
doc.add_picture(
    "gen_files\images\9_page3_Im0.jpg",
    height=docx.shared.Inches(1),
    width=docx.shared.Cm(4),
)
doc.save("gen_files/with_image.docx")
