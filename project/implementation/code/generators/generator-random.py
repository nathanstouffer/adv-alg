# a python file to generate a randomly connected graph according to command line arguments

import random
from sys import argv

def make_key(i, j):
    return str(i) + "," + str(j)

# we assume prob is in [0,1]
def make_graph(num, prob):
    ret = "V " + str(num)
    max = 4                                                                     # maybe change this value?
    for i in range(0, num):                                                     # initialize vertex positions
        x = max*random.random()
        y = max*random.random()
        ret += "\n" + str(i) + " " + str(x) + " " + str(y)
    edges = {}
    for i in range(0, num):                                                     # create the edges
        for j in range(0, num):
            if (i != j):
                if (random.random() < prob):
                    if (make_key(i,j) not in edges and make_key(j,i) not in edges):
                        edges[make_key(i,j)] = [i, j]
    ret += "\nE " + str(len(edges))                                             # add the edges to the output string
    for key in edges:
        ret += "\n" + str(edges[key][0]) + " " + str(edges[key][1])
    return ret

script, num, prob, file_name = argv

graph_string = make_graph(int(num), float(prob))
fout = open(file_name, 'w')
fout.write(graph_string)
fout.close()
