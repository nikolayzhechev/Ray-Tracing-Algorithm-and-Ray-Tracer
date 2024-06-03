from vector import Vector

class Color(Vector):
    """Color class stores RGB values - derived from Vector class"""

    # define hex function
    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        # converts hex to value and devide by 255.0
        x = int(hexcolor[1:3], 16) / 255.0
        y = int(hexcolor[3:5], 16) / 255.0
        z = int(hexcolor[5:7], 16) / 255.0
        
        return cls(x, y, z)