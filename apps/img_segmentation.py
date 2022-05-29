from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from apps.KMeans import KMeans


def segment(image, k):

    # turn img into arr
    img_arr = np.array(image, dtype='int64')

    # get img size
    height, width = image.size

    # k_mean
    model = KMeans(img_arr, k)
    # label each pixel with obj
    labels = model.predict()

    # get median colors to color each obj
    colors = model.get_objects_center(model.objects)

    # new img [x][y][rgb]
    new_img = [[[0 for _ in range(3)] for _ in range(height)] for _ in range(width)]

    # color the new img
    for i in range(width):
        for j in range(height):
            new_img[i][j] = colors[labels[i][j]]

    plt.imshow(new_img)
    plt.savefig("temp_img/newSegImg.jpg")
    return Image.open("temp_img/newSegImg.jpg")





