import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("./data/activity.jpg")
plt.imshow(img)
plt.show()