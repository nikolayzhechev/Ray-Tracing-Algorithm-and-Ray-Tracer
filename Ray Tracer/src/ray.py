class Ray:
    """Defines the ray with origin and direction."""
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()