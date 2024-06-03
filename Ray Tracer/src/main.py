from color import Color
from vector import Vector
from point import Point
from scene import Scene
from engine import RenderEngine
from sphere import Sphere

def main():
    """Main ray tracer entrypoint"""
    # width, height constants
    WIDTH = 320
    HEIGHT = 200
    
    # instantiate Vector for camera view
    camera = Vector(0, 0, -1)
    # objects in array - Sphere, Point, Color
    objects = [Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000"))]
    # define scene and pass objects, camera, w, h to the scene
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    # instantiate render engine
    engine = RenderEngine()
    # create the image andd pass the scene to the rendor method
    image = engine.render(scene)

    # display the image in Jupyter notebook
    image.display()
    
    # file stream to generate the file
    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()