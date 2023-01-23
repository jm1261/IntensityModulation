import numpy as np
import matplotlib.pyplot as plt


def get_region_interest(image,
                        file_name):
    '''
    Allows user to select an area of an image of interest. Plots image as x, y
    coordinates and uses matplotlib ginput to select two regions of interest
    and finds the midpoint between the two coordinates in both x and y. Uses the
    midpoint to return x, y coordinates for a perfect box of constant size. For
    best results, select waveguide edge.
    Args:
        image: <object> PIL image object
        file_name: <string> file name identifier
    Returns:
        x_pixels: <array> x pixel range
        y_pixels: <array> y pixel range
    '''
    fig, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=[20, 14])
    ax.imshow(image)
    ax.set_xlabel(
        'X pixels',
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_ylabel(
        'Y pixels',
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_title(
        file_name,
        fontsize=18,
        fontweight='bold',
        color='black')
    ax.text(
        x=5,
        y=5,
        s='Select Two Points For ROI',
        fontsize=14,
        fontweight='bold',
        color='Red',
        horizontalalignment='left',
        verticalalignment='top')
    fig.show()
    regions = (np.array(plt.ginput(2))).astype(float)
    plt.close(fig)
    midpoint = [
        int((((regions[0])[0]) + ((regions[1])[0])) / 2),
        int((((regions[0])[1]) + ((regions[1])[1])) / 2)]
    x_pixels = [x for x in range(midpoint[0] - 25, midpoint[0] + 21, 1)]
    y_pixels = [y for y in range(midpoint[1] - 15, midpoint[1] + 16, 1)]
    return x_pixels, y_pixels
