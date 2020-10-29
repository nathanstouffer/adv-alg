# a vertex class

import numpy as np

class Vertex:

# CONSTRUCTOR ------------------------------------------------------------------

    def __init__(self, id, x, y):
        self.id = id
        self.x  = x
        self.y  = y

# PUBLIC METHODS ---------------------------------------------------------------

    def set_pos(self, x, y):
        self.x  = x
        self.y  = y

    def __str__(self):
        ret  = self.id + " --- ("
        ret += str(self.x) + "," + str(self.y) + ")"
        return ret


# PRIVATE METHODS --------------------------------------------------------------
