# main file to run the force directed graph algorithm

from sys import argv
import graph
import networkx as nx
import matplotlib.pyplot as plt
from vector2 import *
import subprocess

# ALGORITHM PARAMETERS ---------------------------------------------------------

C = 1
K = 1
tol = 0.1
init_step_length = 5 

# FUNCTIONS --------------------------------------------------------------------

def draw_and_save(g, name, show):
    nx.draw(g.nx_graph(), pos=g.positions(), node_size=25, node_color='g', width=0.1)
    plt.savefig(outdir + "/" + name + ".png", dpi=600)
    if (show):
        plt.show()
    plt.clf()

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

# force directed algorithm that updates vertex positions until converged
def force_directed(g, tol):
    converged = False
    step = init_step_length
    iter = 0
    while not converged:
        delta = 0
        for vert in g.verts:
            f = Vector2(0, 0)
            for adj_vert in g.neighbors(vert):
                mag = spring_force_mag(g, vert, adj_vert)
                f = f + unit_vec(g, vert, adj_vert).scale(mag)
                #print("spring:", mag)
            for other_vert in g.verts:
                if (other_vert != vert):
                    mag = electric_force_mag(g, vert, other_vert)
                    f = f + unit_vec(g, vert, other_vert).scale(mag)
                    #print("electric:", mag)
            #print("mag", f.mag())
            if (f.mag() != 0):
                g.verts[vert].pos += f.normalize().scale(step)
                delta += step**2
                #g.verts[vert].pos = g.verts[vert].pos + f
                #delta += f.mag()*f.mag()
        draw_and_save(g, str(iter), False)
        if (math.sqrt(delta) < tol):
            converged = True
        step = 0.9 * step
        iter += 1
        print("iter:", iter, "delta:", delta, flush=True)
    return g

# CODE -------------------------------------------------------------------------

script, file_name = argv
outdir = "../output/" + file_name.split('/')[-1].split('.')[0]

subprocess.run(['mkdir', outdir])

# RUN THE ALGORITHM ------------------------------------------------------------

g = graph.Graph(file_name)
draw_and_save(g, "init", False)
g = force_directed(g, tol)
draw_and_save(g, "converged", True)
