# a basic graph class
# we use an adjacency list to implement the graph

import networkx as nx
import vertex

class Graph:

# CONSTRUCTOR ------------------------------------------------------------------

    def __init__(self, file_name):
        self.name = file_name.split('/')[-1].split('.')[0]                      # extract file name
        self.read_graph(file_name)                                              # read graph and declare class variables

# PUBLIC METHODS ---------------------------------------------------------------

    # method to compute the euclidean distance between two vertices
    def dist(self, src, trg):
        pass

    # method to return the positions of the vertices in a dictionary format (for displaying the graph)
    def positions(self):
        pass

    # method to return the immediate neighbors of a vertex
    def neighbors(self, vert):
        return self.verts[vert]

    # method to return the nxGraph object to be displayed to the screen
    def nx_graph(self):
        pass

    def __str__(self):
        ret  = "Graph: " + self.name
        ret += "\nVertices"
        for key in self.verts:
            ret += "\n" + str(self.verts[key])
        ret += "\nEdges"
        for key in self.edges:
            ret += "\n" + str(key) + ": " + str(self.edges[key])
        return ret


# PRIVATE METHODS --------------------------------------------------------------

    # method to read the graph in from a file
    def read_graph(self, file_name):
        fin = open(file_name, 'r')
        self.num_verts = int(fin.readline().rstrip().split()[1])                # get the number of vertices in the graph
        self.verts = {}                                                         # set up a dictionary for the vertices
        self.edges = {}                                                         # set up a dictionary for the edges
        for i in range(0, self.num_verts):                                      # initialize vertex storage
            vert = fin.readline().rstrip().split()                              # read in a vertex
            id   = vert[0]
            x    = float(vert[1])
            y    = float(vert[2])
            self.verts[id] = vertex.Vertex(id, x, y)                            # store vertex
            self.edges[id] = []                                                 # set up adjacency list
        self.num_edges = int(fin.readline().rstrip().split()[1])                # get the number of edges in the graph
        for i in range(0, self.num_edges):                                      # set up the edges
            edge = fin.readline().rstrip().split()                              # read in an edge
            u    = edge[0]
            v    = edge[1]
            if (v not in self.edges[u]):                                        # test if the edge is stored in the graph (undirected so symmetry is assumed)
                self.edges[u].append(v)
                self.edges[v].append(u)
        fin.close()
