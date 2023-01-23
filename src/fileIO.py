import json
import numpy as np

from PIL import Image
from pathlib import Path


def load_json(file_path):
    '''
    Extract user variables from json dictionary.
    Args:
        file_path: <string> path to file
    Returns:
        dictionary: <dict> use variables dictionary
    '''
    with open(file_path, 'r') as file:
        return json.load(file)


def read_image(file_path):
    '''
    Load image file.
    Args:
        file_path: <string> path to file
    Returns:
        image: <object> PIL image object
    '''
    image = Image.open(file_path)
    return image
