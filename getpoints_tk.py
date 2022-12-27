"""Get coordinates of points on a picture by clicking (python code).

AUTHOR:

- Emmanuel Briand (Universidad de Sevilla), 2022.

REQUIRES the python packages: tkinter, pillow.

1. Run `L = get_points(IMAGEFILE)` where IMAGEFILE is the adress of an image.
2. A new window appears with the image.
3. Click on the image to select points. They appear in red.
4. When finished, close the image window.
5. The coordinates of the points are now stored in the list L.
"""

from tkinter import *
from PIL import Image, ImageTk

def newsize(width, height, maxwidth, maxheight):
    """Return the width and height of a picture will have after resizing proportionally so that it fulfills
    width <= maxwidth, height <= maxheight
    """
    m = min(maxwidth / width, maxheight / height)
    width , height  = int(width * m), int(height * m)
    return width, height
    

def get_points(imagefile):
    """Show the picture and return the list of coordinates for the clicks.
    
    Close the image window to get the list. 
        
    EXAMPLE:
    
    >>> L = get_points("IMAGES/dipylon_horizontal.jpg")
    
    """
    root = Tk()

    original = Image.open(imagefile)
    ancho, alto = original.size
    ancho, alto = newsize(ancho, alto, 1200, 800)
    original = original.resize((ancho, alto))
                             
    w = Canvas(root, width=ancho, height=alto)
    w.pack()
    
    img = ImageTk.PhotoImage(original)

    w.create_image(0, 0, image=img, anchor="nw")

    def onclick(event):
        X, Y = event.x, event.y
        L.append((X, Y))
        w.create_oval(X, Y, X, Y, width = 5,  outline = 'red', fill='red')
        return None

    L = []
    w.bind("<Button 1>", onclick)
    root.mainloop()
    return L
