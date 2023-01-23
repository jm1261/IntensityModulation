import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plots_image_roi(image,
                    x_pixels,
                    y_pixels,
                    file_name,
                    out_path):
    '''
    Plots image and region of interest as matplotlib imshow.
    Args:
        image: <object> PIL image object
        x_pixels: <array> x pixel range
        y_pixels: <array> y pixel range
        file_name: <string> file name identifier
        out_path: <string> path to save
    Returns:
        None
    '''
    fig, (ax1, ax2) = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=[20, 7])
    ax1.imshow(image)
    rectangle = patches.Rectangle(
        xy=(min(x_pixels), min(y_pixels)),
        width=max(x_pixels) - min(x_pixels),
        height=max(y_pixels) - min(y_pixels),
        linewidth=1,
        edgecolor='r',
        facecolor='none')
    ax1.add_patch(rectangle)
    ax2.imshow(
        (np.array(image))[
            min(y_pixels): max(y_pixels),
            min(x_pixels): max(x_pixels)])
    ax1.set_xlabel(
        'X Pixels',
        fontsize=14,
        fontweight='bold',
        color='black')
    ax1.set_ylabel(
        'Y Pixels',
        fontsize=14,
        fontweight='bold',
        color='black')
    ax2.set_xlabel(
        'X Pixels',
        fontsize=14,
        fontweight='bold',
        color='black')
    ax2.set_ylabel(
        'Y Pixels',
        fontsize=14,
        fontweight='bold',
        color='black')
    ax1.set_title(
        file_name,
        fontsize=18,
        fontweight='bold')
    ax2.set_title(
        'Region of Interest',
        fontsize=18,
        fontweight='bold')
    ax1.tick_params(
        axis='both',
        colors='black',
        labelsize=14)
    ax2.tick_params(
        axis='both',
        colors='black',
        labelsize=14)
    fig.tight_layout()
    plt.savefig(out_path)
    fig.clf()
    plt.cla()
    plt.close(fig)
