# main file to run the force directed graph algorithm

from sys import argv
import graph
import networkx as nx # mayb try pygraphvis
import matplotlib.pyplot as plt

script, file_name = argv

# TEST CODE
g = graph.Graph(file_name)
print(g)

nx.draw(g.nx_graph(), pos=g.positions(), node_size=100, node_color='g')
plt.show()
