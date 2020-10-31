# main file to run the force directed graph algorithm

from sys import argv
import graph
import networkx as nx
import matplotlib.pyplot as plt
from vector2 import *

#Parameters to tune for electric force calculations
C = 1
K = 1

# function to compute the magnitude of the spring force between u and v
def spring_force_mag(g, u, v):
    dist = g.distance(u, v)
    return (dist*dist) / K

# function to compute the magnitude of the spring force between u and v
def electric_force_mag(g, u, v):
    return -(C*K*K) / g.distance(u, v)

# function to compute the unit vector between s and t
def unit_vec(g, s, t):
    s_pos = g.verts[s].pos
    t_pos = g.verts[t].pos
    diff  = t_pos - s_pos
    return diff.normalize()

#Force directed algorithm that updates vertex positions until converged
def force_directed(g, to1):
    init_step_length = 10
    converged = False
    step = init_step_length
    
    while not converged:
        delta = 0
        x = g.positions()
        for vert in g.verts:
            f = Vector2(0, 0)
            for adj_vert in g.edges[vert]:
                f += unit_vec(g, vert, adj_vert).scale(spring_force_mag(g, vert, adj_vert))
            for other_vert in g.verts:
                if other_vert != vert:
                    f += unit_vec(g, vert, other_vert).scale(electric_force_mag(g, vert, other_vert))

            if f.mag() != 0:
                g.verts[vert].pos += f.normalize().scale(step)
                delta += step**2

            print(g.verts[vert].pos)


        if math.sqrt(delta) < to1:
            converged = True
        step = .9 * step
    return x

script, file_name = argv

# TEST CODE
g = graph.Graph(file_name)
#print(g)
#print(g.distance('1','3'))
x = force_directed(g, 5)
nx.draw(g.nx_graph(), pos=g.positions(), node_size=50, node_color='g', width=0.1)
plt.show()
