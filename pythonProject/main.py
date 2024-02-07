import platform
from pathlib import Path
from PIL import Image
import os

def get_image_path(imageDir, imageName):
    # Finding path to image
    if platform.system() == "Windows":
        imagePath = os.path.join(imageDir, imageName)
    else:
        imagePath = Path(imageDir).joinpath(imageName)
    
    return imagePath

def load_image(imagePath):
    # Loading image
    with Image.open(imagePath) as img:
        size = img.size

        print("Successfully loaded Image!\n"
              "Image Size: " + str(size))
        #img = img.thumbnail((img.height, 200))
        pixls = list(img.getdata())

    return [pixls[i:i+img.width] for i in range(0, len(pixls), img.width)]

def rgb_average(rgbTuple):
    average = sum(rgbTuple) / len(rgbTuple)
    return average

def rgb_to_lightness(rgbTuple):
    return (max(rgbTuple) + min(rgbTuple))/2

def rgb_to_luminosity(rgbTuple):
    return 0.21 * rgbTuple[0] + 0.72 * rgbTuple[1] + 0.07 * rgbTuple[2]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imageDir = Path("images")
    imageFileName = "ascii-pineapple.jpg"

    pathToImage = get_image_path(imageDir, imageFileName)

    pixels = load_image(pathToImage)

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
        elif filterVal == "1":
            filterFunc = rgb_to_lightness
        else:
            filterFunc = rgb_to_luminosity
    except Exception as e:
            print(f"Error: {e}")
            print("Invalid value given. Defaulting to Luminosity filter.")

    brightnessMatrix = []
    for x in range(len(pixels)):
        brightnessRow = []
        rowList = [filterFunc(pixel) for pixel in pixels[x]]
        # append list to 2d list
        brightnessMatrix.append(rowList)

    print(brightnessMatrix)
