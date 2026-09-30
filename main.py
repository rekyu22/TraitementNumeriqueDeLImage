from pathlib import Path
import numpy
import matplotlib.pyplot as plt
import skimage as ski

image = ski.io.imread(Path(__file__).with_name("rom.jpeg"))

gImg = ski.color.rgb2gray(image)
plt.imshow(gImg, cmap='gray', vmin=0, vmax=0.7)
plt.show()



"""plt.imshow(image, cmap='gray', vmin=2, vmax=8)"""

"""



yImg = ski.color.rgb2ycbcr(image) 

numpy.shape(image)
numpy.min(image)

numpy.uint8(array), numpy.uint8(array)

ski.transform.resize(image, new_shape, preserve_range=True)


 
matplotlib.pyplot.subplot(nrows, ncols, index) 
 
matplotlib.pyplot.subplot(nrows, ncols, index) 

"""