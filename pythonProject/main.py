import platform

from PIL import Image
import os

def load_image(pathToImage):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imageFileName = "ascii-pineapple.jpg"
    pathToImage = ''

    # Finding path to image
    if platform.system() == "Windows":
        import os
        pathToImage = os.path.join("images", imageFileName)
    else:
        import pathlib as Path
        pathToImage = Path("images").joinpath(imageFileName)


    print(pathToImage)
    print(platform.system())
