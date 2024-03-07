from dataclasses import dataclass, field

import numpy as np

from color import color


@dataclass
class Material:
    color: np.array = field(default_factory=list)
    ambient: float = 0.1
    diffuse: float = 0.9
    specular: float = 0.9
    shininess: float = 200.0

    def __post_init__(self):
        if self is None or len(self.color) < 3:
            self.color = color(1, 1, 1)

    def set_ambient(self, a):
        return material(self.color, a, self.diffuse, self.specular, self.shininess)

    def set_color(self, c):
        return material(c, self.ambient, self.diffuse, self.specular, self.shininess)

    def set_diffuse(self, d):
        return material(self.color, self.ambient, d, self.specular, self.shininess)

    def set_specular(self, s):
        return material(self.color, self.ambient, self.diffuse, s, self.shininess)

    def set_shininess(self, s):
        return material(self.color, self.ambient, self.diffuse, self.specular, s)

    def __eq__(self, other):
        return np.allclose(self.color, other.color) and (
                self.ambient == other.ambient and
                self.diffuse == other.diffuse and
                self.specular == other.specular and
                self.shininess == other.shininess
        )


material = Material
