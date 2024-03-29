import platform
from pathlib import Path
from PIL import Image
import os

MAX_PIXEL_VALUE = 255
IMG_RESIZE_HEIGHT = 200
IMG_RESIZE_WIDTH = 1000

# Finding path to image
def get_image_path(imageDir, imageName):
    """
    function that returns the relative path of the image
    :param imageDir:
    :param imageName:
    :return:
    """
    if platform.system() == "Windows":
        imagePath = os.path.join(imageDir, imageName)
    else:
        imagePath = Path(imageDir).joinpath(imageName)
    
    return imagePath

# Loading image
def load_image(imagePath):
    """
    function that loads an image and resizes it to a desired size
    :param imagePath:
    :return:
    """
    with Image.open(imagePath) as img:
        img.thumbnail((IMG_RESIZE_WIDTH, IMG_RESIZE_HEIGHT))
        size = img.size

        print("Successfully loaded Image!\n"
              "Image Size: " + str(size))
        pixls = list(img.getdata())

    return [pixls[i:i+img.width] for i in range(0, len(pixls), img.width)]

def rgb_average(rgbTuple):
    """
        function that convert rgb to average value of rbg values
        :param rgbTuple:
        :return:
        """
    average = sum(rgbTuple) / len(rgbTuple)
    return average

def rgb_to_lightness(rgbTuple):
    """
        function that convert rgb to lightness value
        :param rgbTuple:
        :return:
        """
    return (max(rgbTuple) + min(rgbTuple))/2

def rgb_to_luminosity(rgbTuple):
    """
    function that convert rgb to luminosity value
    :param rgbTuple:
    :return:
    """
    return 0.21 * rgbTuple[0] + 0.72 * rgbTuple[1] + 0.07 * rgbTuple[2]

def get_user_filter_choice():
    """
    function that returns the appropriate filter chosen by user
    :rtype: object
    """
    # Get Filter input from user
    print("Which filter do you want to use on image?")
    print("Input either 0,1 or 2 for corresponding filters.\n"
          "0. Average\n"
          "1. Lightness\n"
          "2. Luminosity\n")

    try:
        filterVal = input()

        if filterVal == "0":
            filterFunc = rgb_average
            print("Average filter chosen")
        elif filterVal == "1":
            filterFunc = rgb_to_lightness
            print("Lightness filter chosen")
        else:
            filterFunc = rgb_to_luminosity
            print("Luminosity filter chosen")
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid value given. Defaulting to Luminosity filter.")

    return filterFunc

def normalize_brightness_matrix(brightnessMatrix):
    """
    Function that normalizes pixels brightess values
    :param brightnessMatrix:
    :return:
    """
    normalizedBrightnessMatrix = []
    maxPixel = max(map(max, brightnessMatrix))
    minPixel = min(map(min, brightnessMatrix))

    for row in brightnessMatrix:
        rescaledRow = []
        for pixel in row:
            r = MAX_PIXEL_VALUE * (pixel - minPixel)/ float(maxPixel - minPixel)
            rescaledRow.append(r)
        normalizedBrightnessMatrix.append(rescaledRow)

    return normalizedBrightnessMatrix

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imageDir = Path("images")
    imageFileName = "stripes.png"

    pathToImage = get_image_path(imageDir, imageFileName)

    pixels = load_image(pathToImage)

    filterFunc = get_user_filter_choice()

    brightnessMatrix = []
    for x in range(len(pixels)):
        brightnessRow = []
        rowList = [filterFunc(pixel) for pixel in pixels[x]]
        # append list to 2d list
        brightnessMatrix.append(rowList)
    normalizedBrightnessMatrix = normalize_brightness_matrix(brightnessMatrix)

    # convert brightness to ASCII (sorted by thickness)
    # brightness has a range of 0 - 255, while ascii chars are from 0 - 64
    # mapping 255 = 64 therefore e.g.
    # Brightness 180, (180*64)/255 = 45.17
    #  we then round up or down the result
    asciiChar = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    asciiMatrix = []
    for x in range(len(normalizedBrightnessMatrix)):
        asciiRow = []
        for brightnessVal in range(len(normalizedBrightnessMatrix[x])):
            asciiVal = round((normalizedBrightnessMatrix[x][brightnessVal] * (len(asciiChar)-1))/MAX_PIXEL_VALUE)
            asciiRow.append(asciiChar[asciiVal])
            # asciiRow.append(asciiChar[asciiVal])
            # asciiRow.append(asciiChar[asciiVal])
        asciiMatrix.append(asciiRow)

    print(asciiMatrix)

