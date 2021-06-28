# Debugging module

from LivestockCV.core import params
from LivestockCV.core import print_image
from LivestockCV.core import plot_image


def _debug(visual, filename=None):
    """Save or display a visual for debugging.

    Inputs:
    visual   - An image or plot to display for debugging
    filename - An optional filename to save the visual to (default: None)

    :param visual: numpy.ndarray
    :param filename: str
    """
    # Auto-increment the device counter
    params.device += 1
    
    if params.debug == "print":
        # If debug is print, save the image to a file
        print_image(img=visual, filename=filename)
    elif params.debug == "plot":
        # If debug is plot, print to the plotting device
        plot_image(img=visual)
