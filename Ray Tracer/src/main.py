from color import Color
from vector import Vector
from point import Point
from scene import Scene
from engine import RenderEngine
from sphere import Sphere
from material import Material, PlaneMaterial
from light import Light

def main(WIDTH, HEIGHT):
    """Main ray tracer entrypoint"""
    CAMERA = Vector(0, -0.35, -1)
    # define objects - from spec sheet
    OBJECTS = [
        # Ground Plane
        Sphere(
            Point(0, 10000.5, 1),
            10000.0,
            PlaneMaterial(
                color=Color.from_hex("#ADC2B8"),
                ambient=0.2,
                reflection=0.2,
            ),
        ),
        # Blue ball
        Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
        # Pink ball
        Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980"))),
    ]
    
    # define lights - from spec sheet
    LIGHTS = [
        Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
        Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6")),
    ]
    
    # instantiate Vector for camera view
    camera = Vector(0, -0.35, -1)
    # define scene and pass objects, camera, w, h to the scene
    scene = Scene(CAMERA, OBJECTS, LIGHTS, WIDTH, HEIGHT)
    # instantiate render engine
    engine = RenderEngine()
    # create the image andd pass the scene to the rendor method
    image = engine.render(scene)

    # display the image in Jupyter notebook
    image.display()

if __name__ == "__main__":
    main()