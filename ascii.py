import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White


# Getting the character List, Font and Scaling characters for square Pixels

# Reading Input Image

# Converting Color Image to Grayscale

# Extracting height and width from Image

# Defining height and width of each cell==pixel

# Calculating Height and Width of the output Image

# Making a new Image using PIL

# Mapping the Characters
    # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
    # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
    # Draw string at a given position (x,y)

# Inverting Image and removing excess borders

# Saving the new Image
