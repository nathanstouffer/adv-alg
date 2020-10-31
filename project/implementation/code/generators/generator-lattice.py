# a python file to generate a lattice graph according to command line arguments

import random
import math
import sys
from sys import argv

def make_key(i, j):
    return str(i) + "," + str(j)

# we assume prob is in [0,1]
def make_graph(num):
    sqrt = int(math.sqrt(num))
    ret = "V " + str(num)
    max = 4                                                                     # maybe change this value?
    for i in range(0, num):                                                     # initialize vertex positions
        x = max*random.random()
        y = max*random.random()
        ret += "\n" + str(i) + " " + str(x) + " " + str(y)
    edges = {}
    for i in range(0, sqrt-1):                                                  # create the edges
        base = i*sqrt
        for j in range(0, sqrt-1):
            edges[make_key(base+j,base+j+1)]    = [base+j, base+j+1]
            edges[make_key(base+j,base+j+sqrt)] = [base+j, base+j+sqrt]
        edges[make_key(base+sqrt-1,base+sqrt-1+sqrt)] = [base+sqrt-1, base+sqrt-1+sqrt]
    base = sqrt*(sqrt-1)
    for j in range(0, sqrt-1):
        edges[make_key(base+j,base+j+1)]    = [base+j, base+j+1]
    ret += "\nE " + str(len(edges))                                             # add the edges to the output string
    for key in edges:
        ret += "\n" + str(edges[key][0]) + " " + str(edges[key][1])
    return ret

script, num, file_name = argv
num = int(num)
if (int(math.sqrt(num)) != math.sqrt(num)):
    print("num must be a perfect square")
    sys.exit(1)

graph_string = make_graph(num)
fout = open(file_name, 'w')
fout.write(graph_string)
fout.close()
