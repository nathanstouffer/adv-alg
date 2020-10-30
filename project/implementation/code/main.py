# main file to run the force directed graph algorithm

from sys import argv
import graph
import networkx as nx
import matplotlib.pyplot as plt

# function to compute the magnitude of the spring force between u and v
def spring_force_mag(g, u, v):
    pass

# function to compute the magnitude of the spring force between u and v
def electric_force_mag(g, u, v):
    pass

# function to compute the unit vector between s and t
def unit_vec(g, s, t):
    s_pos = g.verts[s].pos
    t_pos = g.verts[t].pos
    diff  = t_pos - s_pos
    return diff.normalize()

script, file_name = argv

# TEST CODE
g = graph.Graph(file_name)
#print(g)
#print(g.distance('1','3'))

nx.draw(g.nx_graph(), pos=g.positions(), node_size=50, node_color='g', width=0.1)
plt.show()
