# colorTransform.py

from color import Color

import numpy as np
from typing import Tuple
import unittest


class ColorTransform:
    def __init__(self, locality: float, *args: Tuple[Color, Color]):
        self.xs = np.stack([np.asarray(k.nrgba) for (k, _) in args], axis=1)
        self.ys = np.stack([np.asarray(v.nrgba) for (_, v) in args], axis=1)
        self.lambda_ = locality

        self.vectorized = np.vectorize(self)
        
    def on_color(self, color: Color):
        tnrgba = self(np.asarray(color.nrgba))
        return Color.from_nrgb(tnrgba[:3])
        
    
    def __call__(self, pixel: np.array):
        """"""
        """
        f(x) is the identify function plus some offset towards each y_i times the e^-distance between x and x_i,
        similar to a radial basis function with features at {(x_i, y_i)}_i
        
        Original equation is:
        f(x) = x + sum_i^n(exp(-l * ||x - x_i||^2) * (y_i - x))
                                     '- d_x -'       '- d_y -'
                                    '--- norm ---'
                           '------- exp ---------'
                                    
        """
        x = pixel
        d_x = ((self.xs ** 2) - (x[:, None] ** 2))
        # d_x = self.xs - x[:, None]
        norm = np.sum(d_x ** 2, axis=0) ** 0.5
        exp = np.exp(-self.lambda_ * norm)
        d_y = self.ys - x[:, None]
        return x + np.sum(exp * d_y, axis=1)
    

class ColorUnitTest(unittest.TestCase):
    def test_color_transform(self):
        orange = Color.from_name("tab:orange")
        green = Color.from_name("tab:green")
        transformation = ColorTransform(1, (orange, green))

        greenish = transformation.on_color(orange)
        self.assertEqual(f"{greenish.hex_code:#0{8}x}", f"{green.hex_code:#0{8}x}")
        
if __name__ == "__main__":
    unittest.main()
