from math import sqrt
import numpy as np

class Sphere:
    """Defines the sphere that is implemented in the scene. It has a center, radius and material."""
    def __init__(self, center, radius, material):
        # use np.array?
        self.center = center
        self.radius = radius
        self.material = material
        # color property can be added

    def intersection(self, ray):
        """Checks if a ray intersects the sphere. Returns the distance to intersection or None if there is no intersection"""
        sphere_to_ray = ray.origin - self.center

        #a = ray.direction.dot_product(ray.direction) #dot(ray.direction, ray.direction)
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            # discriminant > 0 intersects at 2 points
            # discriminant = 0 intersects at 1 point
            # discriminant < 0 does not intersect
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None