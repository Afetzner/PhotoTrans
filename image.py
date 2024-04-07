from PIL import Image
import numpy as np 
import os
from typing import Tuple
import unittest

class PngImage:
    def __init__(self, path: str):
        path = os.path.join(os.getcwd(), path)
        if not os.path.exists(path):
            msg = f"Path {path} does not exist"
            raise ValueError(msg)
        
        name, ext = os.path.splitext(path)
        if ext != ".png":
            msg = f"Must be a .png; image is .{ext}"
            raise ValueError(msg)

        self.path = path
        self.name = name

    def to_pixels(self):
        return np.asarray(Image.open(self.path), dtype=np.uint8)

    def to_npixels(self):
        return self.to_pixels() / 256

class PngImageUnitTestClass(unittest.TestCase):
    def test_to_png(self):
        return
