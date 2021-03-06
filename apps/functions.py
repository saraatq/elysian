import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
from matplotlib import pyplot as plt


def apply_filter(img):
    # laplacian Filter
    applied_filter = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]

    pixels = img.load()
    # to get starting and ending point
    index = len(applied_filter) // 2

    # create the new image
    filteredImg = Image.new('RGB', img.size)
    draw = ImageDraw.Draw(filteredImg)

    for x in range(index, img.width - index):
        for y in range(index, img.height - index):
            acc = [0, 0, 0]
            for i in range(len(applied_filter)):
                for j in range(len(applied_filter)):
                    xn = x + i - index
                    yn = y + j - index
                    pix = pixels[xn, yn]
                    acc[0] += pix[0] * applied_filter[i][j]
                    acc[1] += pix[1] * applied_filter[i][j]
                    acc[2] += pix[2] * applied_filter[i][j]
                draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
    print("done")
    return filteredImg


def show_histogram(image):
    image = np.array(image)

    # tuple to select colors of each channel index
    colors = [(0, "red"), (1, "green"), (2, "blue")]

    # create the histogram plot, with three lines, one for each color
    plt.figure()
    plt.xlim([0, 256])
    for channel_id, c in colors:
        # loop over each rgb value in image to get its histogram
        histogram, bin_edges = np.histogram(
            image[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], histogram, color=c)

    plt.title("Color Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixel count")

    plt.savefig('./temp_img/histogram.jpg')
    histogram = Image.open("./temp_img/histogram.jpg")
    return histogram


def adjustment(image, value):
    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(image)
    if value < 0:
        value *= -1
        # if darkness then  0 < value < 1
        while value > 1:
            value /= float(10)

    output = enhancer.enhance(value)
    return output
