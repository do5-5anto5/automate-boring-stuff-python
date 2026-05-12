from PIL import Image, ImageDraw

img = Image.new('RGBA', (200, 200), 'white')
drawing = ImageDraw.Draw(img)

# Shapes
# ImageDraw methods create shapes on the image.
# fill and outline are optional and default to white.

# Lines
# line(xy, fill, width) draws connected lines.
# width defaults to 1.
drawing.line([(0, 0), (199, 0), (0, 199), (0, 0)], fill='black')

# Rectangles
# rectangle(xy, fill, outline, width) draws a rectangle.
# xy = (left, top, right, bottom).
drawing.rectangle((20, 30, 60, 60), fill='blue')

# Ellipses
# ellipse(xy, fill, outline, width) draws an ellipse or circle.
# xy defines the bounding box.
drawing.ellipse((120, 30, 160, 60), fill='red')

# Polygons
# polygon(xy, fill, outline, width) draws a closed polygon.
# The last point automatically connects to the first.
drawing.polygon(((57,87),(79,62), (94,85), (120,90),(103,113)), fill='green')

# Points
# point(xy, fill) draws pixels.
# xy accepts tuples [(x, y), ...] or flat coords [x1, y1, ...].
# fill defines the color.
for i in range(100, 200, 10):
    drawing.line([(i, 0), (200, i - 100)], fill='purple')

img.show()
img.save('gen_files/images/drawing.png')