"""Python code to get points on an image within a jupyter notebook.

AUTHOR:
   - Emmanuel Briand (Universidad de Sevilla), 2022.
   
REQUIRES: ipywidgets, ipycanvas, imagesize
"""

from ipywidgets import Output, Image
from ipycanvas import Canvas
import imagesize

def newsize(width, height, maxwidth, maxheight):
    r"""Return the width and height that a picture  will have after resizing proportionally so that it fulfills width <= maxwidth, height <= maxheight,
    one of the two inequalities being and equality.
    
    INPUT:
    - with, height: current width and weight
    - maxwidth, maxheight: maximum width and maximum height for the resized images
    """
    m = min(maxwidth / width, maxheight / height)
    width , height  = int(width * m), int(height * m)
    return width, height

def get_points(imagefile):
    r"""Show the image, and return the coordinates of the points clicked.
    
    The origin is the upper left corner (north-west).
    The x-axis is horizontal, from left to right (west to east).
    The y-axis is vertical, from top to bottom (north to south).   
    
    EXAMPLE:
    
    >>> L = get_points("dipylon_horizontal.jpg")
    """
    width, height = imagesize.get(imagefile)
    width, height = newsize(width, height, 960, 720)

    image = Image.from_file(imagefile)

    canvas = Canvas(width=width, height=height)
    canvas.draw_image(image, width=width, height=height)
    display(canvas)

    out = Output()

    L = []

    canvas.fill_style = "red"

    @out.capture()
    def handle_mouse_down(x, y):
        print(f"point at ({x}, {y})")
        canvas.fill_circle(x, y, int(2))
        L.append((x, y))


    canvas.on_mouse_down(handle_mouse_down)

    display(out)
    return L
