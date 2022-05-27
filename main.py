from PIL import Image
from Band_reject_filter import band_filter
from histogram_equalization import histogram_equalization
from img_segmentation import segment
from functions import apply_filter, show_histogram, adjustment

seg_image = "imgs/Image_to_be_segmented.jpg"
noise_image = "imgs/Image_with_periodic_noise.jpg"
equalization_image = "imgs/Image_before_equalization.jpg"

while True:
    print("1. Image segmentation\n2. reduce periodic noise\n3. Histogram Equalization\n4. Apply Filter")
    print("5. show_histogram\n6. change the brightness")
    choice = int(input("please choose: "))

    # Apply Image segmentation
    if choice == 1:
        segment(seg_image, 3)
        break

    elif choice == 2:
        band_filter(noise_image)
        break

    elif choice == 3:
        histogram_equalization(equalization_image)
        break

    elif choice == 4:
        print("\nyou can use \n1. Gaussian Filter \n2. laplacian Filter\n3. input your own filter")
        choice2 = int(input("please choose: "))
        if choice2 == 1:
            # Gaussian Filter
            filter_ = [[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]]
        elif choice2 == 2:
            # laplacian Filter
            filter_ = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
        else:
            row = int(input("please enter rows number: "))
            col = int(input("please enter columns number: "))
            filter_ = []
            for i in range(row):
                filter_.append([])
                for j in range(col):
                    filter_[i].append(int(input()))
            print("done")
        apply_filter(filter_, seg_image)
        break

    elif choice == 5:
        show_histogram(seg_image)
        break

    elif choice == 6:
        print("\nplease choose a mode: \n1. brightness\n2. darkness")
        ch = int(input())
        mode = "brightness" if ch == 1 else "darkness"
        print("\nplease choose a value: ")
        value = float(input())
        adjustment(value, mode, seg_image)
        break
    else:
        print("\nWrong choice! choose again,")
