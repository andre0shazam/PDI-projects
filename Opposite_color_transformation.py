import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.image as mpimg

"""Get the image"""
img = mpimg.imread('Im001.jpg')

"""Ploting the original image"""
plt.imshow(img)
plt.show()

"""Separating the 3 color channels Red, Green and Blue respectively"""
image_r = img[:, :, 0]
image_g = img[:, :, 1]
image_b = img[:, :, 2]

"""Generate a gray image"""
gray_image1 = np.ceil((image_r + image_g + image_b) / 3)

"""Opposite color transformation equations"""
Rg = np.ceil((image_r - image_g) / math.sqrt(2))
Gr = np.ceil(((image_r + image_g) - 2 * image_b) / math.sqrt(6))
By = np.ceil((image_r + image_g + image_b) / math.sqrt(3))

"""Opposite Blue"""
plt.imshow(By, cmap='gray')
plt.show()

"""Opposite Red"""
plt.imshow(Rg, cmap='gray')
plt.show()

"""Oposite Green"""
plt.imshow(Gr, cmap='gray')
plt.show()