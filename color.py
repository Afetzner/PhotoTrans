# Color.py

import matplotlib.colors as mcolors
from typing import Optional
import unittest

class Color:
    def __init__(self, hex_code: str | int):
        if isinstance(hex_code, str):
            self.hex_code = int(hex_code, 16)
        elif isinstance(hex_code, int):
            self.hex_code = hex_code
        else:
            raise TypeError(hex_code)

        r = (self.hex_code // 0x10000) % 0x100
        g = (self.hex_code // 0x100) % 0x100
        b = self.hex_code % 0x100
        self.rgb = (r, g, b)
        self.rgba = (r, g, b, 255)
        # normalized triple of floats [0, 1)
        self.nrgb = (r / 256, g / 256, b / 256)
        self.nrgba = (r / 256, g / 256, b / 256, 1)
        
    @classmethod
    def from_hex(cls, hex_code: str | int):
        return cls(hex_code)

    @classmethod
    def from_name(cls, name: str):
        hex_code = 0x000000
        name = name.lower()
        if ':' in name:
            (table, color) = name.split(':')
            if table == "tab":
                hex_code = mcolors.TABLEAU_COLORS[name].replace('#', "0x")
                
            elif table == "css" or table == "css4":
                hex_code = mcolors.CSS4_COLORS[color].replace('#', "0x")

            elif table == "xkcd":
                hex_code = mcolors.XKCD_COLORS[name].replace('#', "0x")
                
        else:
            r, g, b = mcolors.BASE_COLORS[name]
            hex_code = int(0x1000000 * r) + int(0x10000 * g) + int(0x100 * b)
            
        return cls(hex_code)

    @classmethod
    def from_rgb(cls, rgb):
        r, g, b = rgb
        hex_code = (0x10000 * (r % 256)) + (0x100 * (g % 256)) + (b % 256)
        return cls(hex_code)

    @classmethod
    def from_nrgb(cls, nrgb):
        rgb = (int(256 * x) for x in nrgb)
        return cls.from_rgb(rgb)
            
        
class ColorUnitTest(unittest.TestCase):
    def test_color_base(self):
        c1 = Color.from_hex(0x00C0C0)
        c2 = Color.from_hex("00C0C0")
        c3 = Color.from_hex("0x00C0C0")
        c4 = Color.from_name("c")
        c5 = Color.from_rgb((0, 192, 192))
        c6 = Color.from_nrgb((0, 0.75, 0.75))
        self.assertEqual(c1.hex_code, 0x00C0C0)
        self.assertEqual(c2.hex_code, 0x00C0C0)
        self.assertEqual(c3.hex_code, 0x00C0C0)
        self.assertEqual(c4.hex_code, 0x00C0C0)
        self.assertEqual(c5.hex_code, 0x00C0C0)
        self.assertEqual(c6.hex_code, 0x00C0C0)

    def test_color_tab(self):
        c1 = Color.from_hex(0x9467bd)
        c2 = Color.from_hex("9467bd")
        c3 = Color.from_hex("0x9467bd")
        c4 = Color.from_name("tab:purple")
        self.assertEqual(c1.hex_code, 0x9467bd)
        self.assertEqual(c2.hex_code, 0x9467bd)
        self.assertEqual(c3.hex_code, 0x9467bd)
        self.assertEqual(c4.hex_code, 0x9467bd)

    def test_color_css(self):
        c1 = Color.from_hex(0xff6347)
        c2 = Color.from_hex("ff6347")
        c3 = Color.from_hex("0xff6347")
        c4 = Color.from_name("css:tomato")
        self.assertEqual(c1.hex_code, 0xff6347)
        self.assertEqual(c2.hex_code, 0xff6347)
        self.assertEqual(c3.hex_code, 0xff6347)
        self.assertEqual(c4.hex_code, 0xff6347)

    def test_color_xkcd(self):
        c1 = Color.from_hex(0x8AB8FE)
        c2 = Color.from_hex("8AB8FE")
        c3 = Color.from_hex("0x8AB8FE")
        c4 = Color.from_name("xkcd:carolina blue")
        self.assertEqual(c1.hex_code, 0x8AB8FE)
        self.assertEqual(c2.hex_code, 0x8AB8FE)
        self.assertEqual(c3.hex_code, 0x8AB8FE)
        self.assertEqual(c4.hex_code, 0x8AB8FE)

if __name__ == "__main__":
    unittest.main()
    



        
