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
bg = "black"
if bg == "black":
    bg_code = 0
elif bg = "white":
    bg_code = 255

# Getting the character List, Font and Scaling characters for square Pixels

# Reading Input Image
image = cv2.imread("./data/input1.jpg")

# Converting Color Image to Grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extracting height and width from Image


# Defining height and width of each cell==pixel

# Calculating Height and Width of the output Image

# Making a new Image using PIL
out_image = Image.new("L", (out_width, out_height), bg_code)
draw = ImageDraw.Draw(out_image)

# Mapping the Characters
    # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
    # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
    # Draw string at a given position (x,y)

# Inverting Image and removing excess borders

# Saving the new Image
