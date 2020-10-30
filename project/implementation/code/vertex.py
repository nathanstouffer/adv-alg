# a vertex class

import numpy as np
import vector2

class Vertex:

# CONSTRUCTOR ------------------------------------------------------------------

    def __init__(self, id, vec2):
        self.id = id
        self.pos = vec2

# PUBLIC METHODS ---------------------------------------------------------------

    def x(self):
        return self.pos.x

    def y(self):
        return self.pos.y

    def set_pos(self, vec):
        self.pos.x  = x
        self.pos.y  = y

    def __str__(self):
        ret  = self.id + " --- ("
        ret += str(self.x()) + "," + str(self.y()) + ")"
        return ret


# PRIVATE METHODS --------------------------------------------------------------
