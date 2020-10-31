# a basic vector in \R^2

import math

class Vector2:

# CONSTRUCTOR ------------------------------------------------------------------

    def __init__(self, x, y):
        self.x  = x
        self.y  = y

# PUBLIC METHODS ---------------------------------------------------------------

    def normalize(self):
        return self.scale(1/self.mag())

    def mag(self):
        dist = self.x*self.x + self.y*self.y
        return math.sqrt(dist)

    def scale(self, scalar):
        return Vector2(scalar*self.x, scalar*self.y)

    # other must be of type Vector2
    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    # other must be of type Vector2
    def __sub__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

# PRIVATE METHODS --------------------------------------------------------------
