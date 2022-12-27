# getpoints

Get points coordinates on an image by clicking in a python jupyter notebook.

Requires: ipywidgets, ipycanvas, imagesize.

## How to use

1. In a jupyter notebook with python kernel, import `get_points.py` (or copy, paste and run its content). 
2. In another cell, run `L = get_points("XXX")` where XXX is the path for an image file. The image should show up in the notebook.
3. Click on the points you want to select with the mouse on the image. Each selected point is marked in red. Its coordinates appear below the image and is appended to the list `L`.
4. In another cell, you can access to the content of `L`.
5. To restart the point selection, run again the cell with `L = get_points("XXX")`

See the sample notebook for an example.

## The story

This was inspired by the nice problem ["Volume of Vase" pedagogical activity](https://services.math.duke.edu/education/webfeatsII/gdrive/Team%20A/OurPage.htm) (about numerical integration). It can be used also to have students work with interpolation.

## Example

Here is the screen capture of an example.

<img src="screencapture.png" width=800>
