# ColorMap.py

import sys
from PIL import Image
from image import PngImage
from color import Color
from colorTransform import ColorTransform
import numpy as np

def chroma():
    image = PngImage("chroma_wheel.png")
    purple = Color.from_rgb((145, 69, 126))
    cyan =   Color.from_name("css:cyan")
    green =  Color.from_rgb((122, 192, 89))
    red =    Color.from_name("tab:red")
    transformation = ColorTransform(4, (purple, cyan), (green, red))
    transd_pixels = np.apply_along_axis(transformation, axis=2, arr=image.to_npixels())
    transd_image = Image.fromarray((transd_pixels * 255).astype(np.uint8))
    transd_image.save("chroma_wheel_transformed.png")

def grapes():
    image = PngImage("grapes.png")
    purple = Color.from_rgb((145, 69, 126))
    cyan =   Color.from_name("css:cyan")
    green =  Color.from_rgb((122, 192, 89))
    red =    Color.from_name("tab:red")

    pairs = ((purple, cyan), (green, red))
    transformation = ColorTransform(4, *pairs)
    transd_pixels = np.apply_along_axis(transformation, axis=2, arr=image.to_npixels())
    transd_image = Image.fromarray((transd_pixels * 255).astype(np.uint8))
    transd_image.save("grapes_transformed.png")

def back1():
    image  = PngImage("back1.png")
    pixels = image.to_npixels()
    alpha  = np.ones(shape=pixels.shape[:2], dtype=np.float32)
    pixels = np.concatenate((pixels, alpha[..., np.newaxis]), axis=-1)

    black  = Color.from_rgb((0, 0, 0))
    white = Color.from_rgb((255, 255, 255))
    
    grey   = Color.from_rgb((3, 53, 64))
    salmon = Color.from_rgb((235, 145, 119))
    yellow = Color.from_rgb((255, 234, 169))
    purple = Color.from_rgb((117, 96, 111))
    
    tblue  = Color.from_rgb((91, 207, 250))
    tpink  = Color.from_rgb((254, 171, 185))
    tdblue = Color.from_rgb((6, 164, 223))

    pairs  = ((purple, tdblue), (salmon, tpink), (yellow, white), (black, black))
    
    transformation = ColorTransform(3, *pairs)
    transd_pixels = np.apply_along_axis(transformation, axis=2, arr=pixels)
    transd_image = Image.fromarray((transd_pixels * 255).astype(np.uint8))
    transd_image.save("back1_transformed.png")


if __name__ == "__main__":
    back1()
    
