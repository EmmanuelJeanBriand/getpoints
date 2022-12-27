# getpoints

Get points coordinates on an image by clicking in a python or sagemath jupyter notebook.

Requires: *ipywidgets*, *ipycanvas*, *imagesize*.

## How to use

1. In a jupyter notebook with python kernel, import the function `get_points` from the file `getpoints.py` (or copy, paste and run its content). 
2. In another cell, run `L = get_points("IMAGEFILE")` where IMAGEFILE is the path for an image file. The image should show up in the notebook.
3. Click on the points you want to select with the mouse on the image. Each selected point is marked in red. Its coordinates appear below the image and is appended to the list `L`.
4. In another cell, you can access to the content of `L`.
5. To restart the point selection, run again the cell with `L = get_points("IMAGEFILE")`

## Example

Here is the screen capture of an example.

<img src="screencapture.png" width=800>

---

## Alternative

The implementation in the file `getpoints_tk.py` is an alternative using the modules *tk* and *pillow* instead of *ipywigets*,  *ipycanvas* and *imagesize*.

### How to use the alternative `get_points

1. Import or load `get_points` from `getpoints_tk.py`
2. Run `L = get_points("IMAGEFILE")` where IMAGEFILE is the path of an image.
3. A new window appears with the image.
4. Click on the image to select points. They appear in red.
5. When finished, close the image window.
6. The coordinates of the points are now stored in the list L.

## The story

This was inspired by the nice pedagogical activity ["Volume of Vase"](https://services.math.duke.edu/education/webfeatsII/gdrive/Team%20A/OurPage.htm) (about numerical integration). This updates the tools for this activity. It can also used to work on interpolation.
