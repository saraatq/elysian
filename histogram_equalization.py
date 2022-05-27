import math
import numpy as np
from PIL import Image, ImageDraw


def histogram_equalization(img):
    image = Image.open(img)
    image = image.convert('L')
    image.show()
    img_arr = np.array(image)
    print(len(img_arr), len(img_arr[0]))
    # create list of values 0-255
    pixels = [x for x in range(256)]

    # set width and height of image
    height, width = image.size
    size = width * height
    calc = {}

    # count every pixel appear in image
    for x in range(width):
        for y in range(height):
            pixel = img_arr[x][y]
            if pixel not in calc:
                calc[pixel] = 0
            calc[pixel] += 1

    # get frequency probabilities
    for key in calc:
        calc[key] = calc[key] / size

    # get cumulative probability
    prevCF = 0
    for i in range(256):
        if i in calc:
            prevCF += calc[i]
            calc[i] = math.floor(prevCF * 255)

    # draw the new image
    newImg = Image.new('L', image.size)
    draw = ImageDraw.Draw(newImg)

    for x in range(width):
        for y in range(height):
            pixel = img_arr[x][y]
            draw.point((y, x), calc[pixel])

    newImg.show()
