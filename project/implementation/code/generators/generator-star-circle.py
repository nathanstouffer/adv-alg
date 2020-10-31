# a python file to generate a star-circle graph according to command line arguments

import random
from sys import argv

def make_key(i, j):
    return str(i) + "," + str(j)

def make_graph(num):
    ret = "V " + str(num)
    max = 4                                                                     # maybe change this value?
    for i in range(0, num):                                                     # initialize vertex positions
        x = max*random.random()
        y = max*random.random()
        ret += "\n" + str(i) + " " + str(x) + " " + str(y)
    edges = {}
    for i in range(1, num-1):                                                   # create the edges
        edges[make_key(i,0)]   = [i, 0]
        edges[make_key(i,i+1)] = [i, i+1]
    edges[make_key(num-1,0)] = [num-1,0]
    edges[make_key(num-1,1)] = [num-1,1]
    ret += "\nE " + str(len(edges))                                             # add the edges to the output string
    for key in edges:
        ret += "\n" + str(edges[key][0]) + " " + str(edges[key][1])
    return ret

script, num, file_name = argv

graph_string = make_graph(int(num))
fout = open(file_name, 'w')
fout.write(graph_string)
fout.close()
