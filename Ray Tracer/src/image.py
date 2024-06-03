from PIL import Image as PILImage
import numpy as np
from io import BytesIO
from IPython.display import display, Image as IPImage

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # loop w, h with list comprehension
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    # define a function that sets pixel with self, x, y, color
    def set_pixels(self, x, y, col):
        self.pixels[y][x] = col

    # define write function (to file or to Jupyter notebook)
    def write_ppm(self, img_file):
        def to_byte(c):
            # checks for ppm file
            return round(max(min(c * 255, 255), 0))
            
       # write the image in ppm format
        img_file.write("P3 {} {}\n255\n".format(self.width, self.height))
        
        for row in self.pixels:
            for color in row:
                img_file.write(
                    "{} {} {} ".format(
                        to_byte(color.x), to_byte(color.y), to_byte(color.z)
                    )
                )
            img_file.write("\n")

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

