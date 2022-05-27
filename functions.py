import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
from matplotlib import pyplot as plt


def apply_filter(applied_filter, image):
    img = Image.open(image)
    img.show()
    pixels = img.load()
    index = len(applied_filter) // 2
    filterImg = Image.new('RGB', img.size)
    draw = ImageDraw.Draw(filterImg)
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

    filterImg.show()


def show_histogram(img):
    image = Image.open(img)
    image = np.array(image)
    plt.imshow(image)
    plt.show()
    # tuple to select colors of each channel line
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)

    # create the histogram plot, with three lines, one for
    # each color
    plt.figure()
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            image[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], histogram, color=c)

    plt.title("Color Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixel count")

    plt.show()


def adjustment(factor, mode, img):
    # read the image
    image = Image.open(img)
    image.show()
    # img_arr = np.array(image)
    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(image)
    if mode == "darkness":
        while factor > 1:
            factor /= float(10)
    output = enhancer.enhance(factor)
    # for x in range(len(img_arr)):
    #     for y in range(len(img_arr[0])):
    #         for ch in range(len(img_arr[0][0])):
    #             img_arr[x][y][ch] *= factor
    #             if img_arr[x][y][ch] > 255:
    #                 img_arr[x][y][ch] = 255
    #             elif img_arr[x][y][ch] < 0:
    #                 img_arr[x][y][ch] = 0
    # Image.fromarray(img_arr).show()
    output.show()
