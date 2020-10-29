# a script to create a gif out of the pngs that we create
# as graph visualizations

import imageio

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave(outpath, images)
