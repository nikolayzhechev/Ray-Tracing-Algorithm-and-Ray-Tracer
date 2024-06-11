from image import Image
from ray import Ray
from color import Color
from scene import Scene
from point import Point

class RenderEngine:
    MAX_DEPTH = 5
    MIN_DISPLACE = 0.0001
    
    # define render function that takes the scene as an argument
    def render(self, scene):
        # define w, h
        width = scene.width
        height = scene.height
        
        # define aspect ratio w / h
        aspect_ratio = float(width) / height

        # left most exterme of x0, x1
        x0 = -1
        x1 = +1
        # how much we need to move in x coordinates (xstep), delta (x1 - x0) / width - 1
        xstep = (x1 - x0) / (width - 1)

        # repeat for y / aspect ratio
        y0 = -1 / aspect_ratio
        y1 = +1 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)
        
        # define camera from scene
        camera = scene.camera
        # define pixels from image
        pixels = Image(width, height)
        
        # loop through w, h
        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                # instantiate Ray with camera and point class(x,y) - camera
                ray = Ray(camera, Point(x, y) - camera)
                # take the result and put it in the pixels.set_pixels(i,j,self.ray_trace(ray, scene)) to render
                pixels.set_pixels(i, j, self.ray_trace(ray, scene))
            # print render progress
            print("Render progress: {:3.0f}%".format(float(j) / float(height) * 100), end="\r")
                
        return pixels

    # define ray trace function
    def ray_trace(self, ray, scene, depth = 0):
        color = Color(0, 0, 0)
        # find the nearest object hit and distance by the ray in the scene
        hit_distance, hit_object = self.find_nearest_object(ray, scene)

        # check if hit object is none and return bg color
        if hit_object is None:
            return color
            
        # find the hit position
        hit_position = ray.origin + ray.direction * hit_distance
        hit_normal = hit_object.normal(hit_position)
        # find the hit color and increment (accumulate) - uses new function that takes the hit object, hit position and scene
        color += self.find_object_color(hit_object, hit_position, hit_normal, scene)

        # calculate depth and reflection
        if depth < self.MAX_DEPTH:
            new_ray_pos = hit_position + hit_normal * self.MIN_DISPLACE
            new_ray_dir = (
                ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            )
            new_ray = Ray(new_ray_pos, new_ray_dir)
            # Attenuate the reflected ray by the reflection coefficient (reflection looses energy when ray is bounicng on every object)
            color += (
                self.ray_trace(new_ray, scene, depth + 1) * hit_object.material.reflection
            )
            
        return color

    def find_nearest_object(self, ray, scene):
        # define minimum distance and hit object
        min_distance = None
        hit_object = None
        
        # loop through every object in the scene
        for obj in scene.objects:
            # distance equals object intersects the ray
            distance = obj.intersection(ray)

            if distance is not None and (hit_object is None or distance < min_distance):
                min_distance = distance
                hit_object = obj
            
        return (min_distance, hit_object)
            

    def find_object_color(self, hit_object, hit_position, normal, scene):
        # define material, color, camera(camera - hit position) and color(ambient times color) variables
        material = hit_object.material
        obj_color = material.color_at(hit_position)
        to_camera = scene.camera - hit_position
        color = material.ambient * Color.from_hex("#000000")
        specular_k = 50

        # loop over every light and calc shading
        for light in scene.lights:
            # instantiate ray with hit position and light position minus hit position
            to_light = Ray(hit_position, light.position - hit_position)
            # diffuse shading (Lambert) must be posative
            color += (obj_color * material.diffuse * max(normal.dot_product(to_light.direction), 0))
            
            # Specular shading (Bling-Phong) must be posative
            half_vector = (to_light.direction + to_camera).normalize()
            color += light.color * material.specular * max(normal.dot_product(half_vector), 0) ** specular_k
        
        return color
        

