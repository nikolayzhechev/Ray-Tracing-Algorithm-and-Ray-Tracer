
class Sphere:
    """Defines the sphere that is implemented in the scene. It has a center, radius and material."""
    def __init__(self, center, radius, material):
        # use np.array?
        self.center = center
        self.radius = radius
        self.material = material
        # color property can be added