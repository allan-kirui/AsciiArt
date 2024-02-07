import platform
from pathlib import Path
from PIL import Image
import os

def get_image_path(imageName):
    # Finding path to image
    if platform.system() == "Windows":
        imagePath = os.path.join("images", imageFileName)
    else:
        imagePath = Path("images").joinpath(imageFileName)
    
    return imagePath

def load_image(imagePath):
    # Loading image
    with Image.open(pathToImage) as img:
        size = img.size

        print("Successfully loaded Image!\n"
              "Image Size: " + str(size))

        pixls = img.load()

    return pixls

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    imageFileName = "ascii-pineapple.jpg"

    pathToImage = get_image_path(imageFileName)

    pixels = load_image(pathToImage)

    print(pixels)


