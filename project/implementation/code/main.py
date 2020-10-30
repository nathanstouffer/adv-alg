# main file to run the force directed graph algorithm

from sys import argv
import graph
import networkx as nx # mayb try pygraphvis
import matplotlib.pyplot as plt

script, file_name = argv

# TEST CODE
g = graph.Graph(file_name)
#print(g)
#print(g.distance('1','3'))

nx.draw(g.nx_graph(), pos=g.positions(), node_size=50, node_color='g', width=0.1)
plt.show()
nx.draw(g.nx_graph(), node_size=50, node_color='g', width=0.1)
plt.show()
nx.draw_circular(g.nx_graph(), node_size=50, node_color='g', width=0.1)
plt.show()
