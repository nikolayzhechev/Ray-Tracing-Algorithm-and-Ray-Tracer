from PIL import Image as PILImage
import numpy as np
from io import BytesIO
from IPython.display import display, Image as IPImage
import os

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # loop w, h with list comprehension
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    # define a function that sets pixel with self, x, y, color
    def set_pixels(self, x, y, col):
        self.pixels[y][x] = col

    # display results in Jupyter notebook
    def to_pil_image(self):
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for y in range(self.height):
            for x in range(self.width):
                color = self.pixels[y][x]
                array[y, x, 0] = to_byte(color.x)
                array[y, x, 1] = to_byte(color.y)
                array[y, x, 2] = to_byte(color.z)
        return PILImage.fromarray(array)

    def display(self):
        pil_img = self.to_pil_image()
        with BytesIO() as f:
            pil_img.save(f, format='PNG')
            display(IPImage(data=f.getvalue(), format='png'))
            
        save_path = "output_image.png"
        pil_img.save(save_path, format='PNG')
