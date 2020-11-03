# a script to create a gif out of the pngs that we create
# as graph visualizations

import imageio
from sys import argv
import subprocess
import networkx as nx
import matplotlib.pyplot as plt
import graph

def save_img(title):
    plt.clf()
    g = graph.Graph(dir + "/" + title + ".grph")
    nx.draw(g.nx_graph(), pos=g.positions(), node_size=25, node_color='g', width=0.1)
    plt.savefig(dir + "/" + title + ".png", dpi=600)

def png_name(title):
    return dir + "/" + title + ".png"

script, dir, step = argv

images = []

save_img("init")
fin = png_name("init")
images.append(imageio.imread(fin))
subprocess.run(['rm', fin])

run = True
file_num = 0
while (run):
    try:
        save_img(str(file_num))
        fin = png_name(str(file_num))
        images.append(imageio.imread(fin))
        subprocess.run(['rm', fin])
        file_num += int(step)
    except FileNotFoundError:
        run = False

# add multiple times so it is longer on converged frame
save_img("converged")
fin = png_name("converged")
images.append(imageio.imread(fin))
images.append(imageio.imread(fin))
images.append(imageio.imread(fin))
images.append(imageio.imread(fin))
subprocess.run(['rm', fin])

file_name = dir.split("/")[-1]
if (file_name == ''):
    file_name = dir.split("/")[-2]
file_name = "../../gifs/" + file_name + ".gif"
subprocess.run(['rm', file_name])
imageio.mimsave(file_name, images, duration=1.5)
