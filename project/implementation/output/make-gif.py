# a script to create a gif out of the pngs that we create
# as graph visualizations

import imageio
from sys import argv
import subprocess

script, dir, step = argv

images = []
images.append(imageio.imread(dir + "/init.png"))

run = True
file_num = 0
while (run):
    try:
        images.append(imageio.imread(dir + "/" + str(file_num) + ".png"))
        file_num += int(step)
    except FileNotFoundError:
        run = False

# add multiple times so it is longer on converged frame
images.append(imageio.imread(dir + "/converged.png"))
images.append(imageio.imread(dir + "/converged.png"))
images.append(imageio.imread(dir + "/converged.png"))

file_name = "../gifs/" + dir.split("/")[0] + ".gif"
subprocess.run(['rm', file_name])
imageio.mimsave(file_name, images, duration=1.5)
