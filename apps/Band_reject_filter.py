import imageio
from scipy import fftpack
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def band_filter(image):
    try:
        image = image.resize((800, 800))

        red, green, blue = image.split()

        red_arr = np.array(red)
        green_arr = np.array(green)
        blue_arr = np.array(blue)

        # from spatial to freq domain and shift it
        fft_red = fftpack.fftshift(fftpack.fft2(red_arr))
        fft_green = fftpack.fftshift(fftpack.fft2(green_arr))
        fft_blue = fftpack.fftshift(fftpack.fft2(blue_arr))

        # create band pass filter image
        height, width = x, y = red_arr.shape
        band_pass = Image.new("L", (width, height), color=1)
        draw1 = ImageDraw.Draw(band_pass)

        # bigger circle
        e_x, e_y = 170, 170
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        draw1.ellipse(bbox, fill=0)

        # smaller circle
        e_x, e_y = 40, 40
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        draw1.ellipse(bbox, fill=1)

        plt.imshow(band_pass)
        plt.savefig("temp_img/filter.jpg")
        filterIMG = Image.open("temp_img/filter.jpg")

        # apply the filter
        band_pass_arr = np.array(band_pass)

        red_filter = np.multiply(fft_red, band_pass_arr)
        green_filter = np.multiply(fft_green, band_pass_arr)
        blue_filter = np.multiply(fft_blue, band_pass_arr)

        # shift it back from freq domain to spatial domain
        ifft_red = fftpack.ifft2(fftpack.ifftshift(red_filter))
        ifft_green = fftpack.ifft2(fftpack.ifftshift(green_filter))
        ifft_blue = fftpack.ifft2(fftpack.ifftshift(blue_filter))

        imageio.imsave('./temp_img/fft-then-ifftred.jpg', ifft_red.astype(np.uint8))
        imageio.imsave('./temp_img/fft-then-ifftgreen.jpg', ifft_green.astype(np.uint8))
        imageio.imsave('./temp_img/fft-then-ifftblue.jpg', ifft_blue.astype(np.uint8))

        red_img = Image.open("./temp_img/fft-then-ifftred.jpg")
        green_img = Image.open("./temp_img/fft-then-ifftgreen.jpg")
        blue_img = Image.open("./temp_img/fft-then-ifftblue.jpg")

        output = Image.merge("RGB", (red_img, green_img, blue_img))
        return [filterIMG, output]

    # ValueError: not enough values to unpack (expected 3, got 1)
    except ValueError:
        # if the image is gray scale

        # turn img to array
        image = image.resize((500, 500))
        img_arr = np.array(image)

        fft = fftpack.fftshift(fftpack.fft2(img_arr))

        band_pass = Image.new("L", (img_arr.shape[1], img_arr.shape[0]), color=1)

        x, y = img_arr.shape

        draw1 = ImageDraw.Draw(band_pass)

        e_x, e_y = 185, 185
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        draw1.ellipse(bbox, fill=0)

        e_x, e_y = 45, 45
        bbox = ((x / 2) - (e_x / 2), (y / 2) - (e_y / 2), (x / 2) + (e_x / 2), (y / 2) + (e_y / 2))
        draw1.ellipse(bbox, fill=1)

        plt.imshow(band_pass)
        plt.savefig("temp_img/filter.jpg")
        filterIMG = Image.open("temp_img/filter.jpg")

        band_pass_arr = np.array(band_pass)
        filtered = np.multiply(fft, band_pass_arr)

        ifft = fftpack.ifft2(fftpack.ifftshift(filtered))
        imageio.imsave("temp_img/fft-then-ifft.jpg", ifft.astype(np.uint8))
        output = Image.open("temp_img/fft-then-ifft.jpg")

        return [filterIMG, output]

