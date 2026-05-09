from PIL import ImageColor

# get color RGBA value
ImageColor.getcolor('red', 'RGBA')
# (255, 0, 0, 255)

ImageColor.getcolor('Black', 'RGBA')
# (0, 0, 0, 255)

ImageColor.getcolor('chocolate', 'RGBA')
# (210, 105, 30, 255)

ImageColor.getcolor('CornflowerBlue', 'RGBA')
# (100, 149, 237, 25)

# get all colors from ImageColor
colors = list(ImageColor.colormap)
print(colors)