from color import Color

class Light():
    """The light class represents a point of light in a cerain color with a position"""
    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color