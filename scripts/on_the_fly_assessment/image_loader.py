"""
author: Fang Ren (SSRL), Robert Tang-Kong
version: 1.1

"""
import fabio
import numpy as np


def load_image(imageFullname):
    # open tiff image
    im = fabio.open(imageFullname)
    # input image object into a numpy array
    imArray = im.data
    return imArray
