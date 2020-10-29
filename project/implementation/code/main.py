# main file to run the force directed graph algorithm

from sys import argv
import graph

script, file_name = argv

# TEST CODE
g = graph.Graph(file_name)
print(g)
