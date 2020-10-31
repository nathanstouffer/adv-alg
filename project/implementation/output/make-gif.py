# a script to create a gif out of the pngs that we create
# as graph visualizations

import imageio
from sys import argv

script, dir, step = argv

images = []
run = True
file_num = 0
while (run):
    try:
        images.append(imageio.imread(dir + "/" + str(file_num) + ".png"))
        file_num += int(step)
    except FileNotFoundError:
        run = False

images.append(imageio.imread(dir + "/converged.png"))
imageio.mimsave("../gifs/" + dir.split("/")[0] + ".gif", images)
