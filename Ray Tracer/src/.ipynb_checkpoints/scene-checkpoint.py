class Scene:
    """Defines the scene needed for rendering via the rendering engine"""
    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height