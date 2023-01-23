from src.fileIO import read_image
from src.plotting import plots_image_roi
from src.userinput import get_region_interest


def find_region_inetest(file_path,
                        file_name,
                        out_path):
    '''
    Process region of interest image.
    Args:
        file_path: <string> path to region of interest file
        file_name: <string> file name identifier
        out_path: <string> path to save roi file
    Returns:
        x_pixels: <array> x pixel range
        y_pixels: <array> y pixel range
    '''
    roi_image = read_image(file_path)
    x_pixels, y_pixels = get_region_interest(
        image=roi_image,
        file_name=file_name)
    plots_image_roi(
        image=roi_image,
        x_pixels=x_pixels,
        y_pixels=y_pixels,
        file_name=file_name,
        out_path=out_path)
    return x_pixels, y_pixels