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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imageDir = Path("images")
    imageFileName = "ascii-pineapple.jpg"

    pathToImage = get_image_path(imageDir, imageFileName)

    pixels = load_image(pathToImage)

    print("Iterating through pixels (R,G,B): ")
    for x in range(len(pixels)):
        for y in range(len(pixels[x])):
            pixel = pixels[x][y]
            print(pixel)

