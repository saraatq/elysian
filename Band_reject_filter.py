import imageio
from scipy import fftpack
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def band_filter(img):
    image = Image.open(img)
    image.show()
    try:
        # image = image.resize((800, 800))
        red, green, blue = image.split()
        image1_np = np.array(image)
        red_arr = np.array(red)
        green_arr = np.array(green)
        blue_arr = np.array(blue)
        fft_red = fftpack.fftshift(fftpack.fft2(red_arr))
        fft_green = fftpack.fftshift(fftpack.fft2(green_arr))
        fft_blue = fftpack.fftshift(fftpack.fft2(blue_arr))
        # print(np.shape(green_np))
        #
        # print(np.shape(fftred))
        low_pass = Image.new("L", (red_arr.shape[1], red_arr.shape[0]), color=1)
        # print(np.shape(low_pass))
        draw1 = ImageDraw.Draw(low_pass)
        x, y = red_arr.shape[0], red_arr.shape[1]
        e_x, e_y = 170, 170
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        # print(bbox)
        draw1.ellipse(bbox, fill=0)
        e_x, e_y = 40, 40
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        draw1.ellipse(bbox, fill=1)
        low_pass_arr = np.array(low_pass)
        plt.imshow(low_pass)
        plt.show()
        red_filter = np.multiply(fft_red, low_pass_arr)
        green_filter = np.multiply(fft_green, low_pass_arr)
        blue_filter = np.multiply(fft_blue, low_pass_arr)
        ifft_red = fftpack.ifft2(fftpack.ifftshift(red_filter))
        ifft_green = fftpack.ifft2(fftpack.ifftshift(green_filter))
        ifft_blue = fftpack.ifft2(fftpack.ifftshift(blue_filter))

        imageio.imsave('fft-then-ifftred.jpg', ifft_red.astype(np.uint8))
        imageio.imsave('fft-then-ifftgreen.jpg', ifft_green.astype(np.uint8))
        imageio.imsave('fft-then-ifftblue.jpg', ifft_blue.astype(np.uint8))

        red_img = Image.open("./fft-then-ifftred.jpg")
        green_img = Image.open("./fft-then-ifftgreen.jpg")
        blue_img = Image.open("./fft-then-ifftblue.jpg")

        output = Image.merge("RGB", (red_img, green_img, blue_img))
        output.show()

    # ValueError: not enough values to unpack (expected 3, got 1)
    except ValueError:
        # turn img to array
        # image = image.resize((500, 500))
        img_arr = np.array(image)
        fft = fftpack.fftshift(fftpack.fft2(img_arr))
        # print(np.shape(fft))
        low_pass = Image.new("L", (img_arr.shape[1], img_arr.shape[0]), color=1)
        # print(np.shape(low_pass))
        draw1 = ImageDraw.Draw(low_pass)

        x, y = img_arr.shape[0], img_arr.shape[1]
        e_x, e_y = 185, 185
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        # print(bbox)
        draw1.ellipse(bbox, fill=0)
        e_x, e_y = 45, 45
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        draw1.ellipse(bbox, fill=1)
        low_pass_arr = np.array(low_pass)
        plt.imshow(low_pass)
        plt.show()
        filtered = np.multiply(fft, low_pass_arr)
        ifft = fftpack.ifft2(fftpack.ifftshift(filtered))
        imageio.imsave('fft-then-ifft.jpg', ifft.astype(np.uint8))
        image = Image.open("./fft-then-ifft.jpg")
        image.show()

