from PIL import Image
import numpy as np
from KMeans import KMeans
import matplotlib.pyplot as plt
import cv2


def segment(img, k):

    # load image
    image = Image.open(img)

    # show the image
    plt.imshow(image)
    plt.show()

    # turn img into arr
    img_arr = np.array(image)

    # 3d array to 2d array
    img_arr = img_arr.reshape((-1, 3))

    # get img sizes
    y, x = image.size
    z = 3

    # k_mean
    model = KMeans(k)
    labels = model.predict(img_arr)

    # setting avg colors
    colors = model.get_cluster_center(model.clusters)

    # new img
    new_img = np.zeros((x*y, z), dtype="uint8")

    # color the img

    for i in range(new_img.shape[0]):
        new_img[i] = colors[labels[i]]

    new_img = np.reshape(new_img, (x, y, z))
    plt.imshow(new_img)
    plt.show()





