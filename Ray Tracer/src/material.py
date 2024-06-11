from color import Color

class Material():
    """Material class includes properties that define how it reacts to light"""
    def __init__(self, color=Color.from_hex("#FFFFFF"), ambient=0.05, diffuse=1.0, specular=1.0, reflection=0.2):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    # define color_at function
    def color_at(self, position):
        return self.color

# define plane material class (open for extention for different material effects)
class PlaneMaterial():
    def __init__(self, color=Color.from_hex("#CACACA"), ambient=0.05, diffuse=1.0, specular=1.0, reflection=0.2):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection
        
    def color_at(self, position):
        return self.color
