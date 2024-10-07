import os
from array import array

joke_path = []
#'/home/chris/PycharmProjects/TTA/app_images/jokes'
foldersx = []
pngFilesx = []
background_img2x = []
meme_imagesx = []
dice_imgx = []
jpeg_imgsx = []

class ImageBank:

    def __init__(self):
        self.background_img2x = []
        self.pngFilesx = pngFilesx
        self.background_img2x = background_img2x
        self.meme_images = []
        self.dice_img = []
        self.jpeg_imgs = jpeg_imgsx

        for dirpath, dirnames,filenames in os.walk('/home/chris/PycharmProjects/TTA/app_images/backgrounds'):
            for filename in filenames:
                if filename.endswith(".png"):
                    pngFilesx.append(filename)
                    background_img2x.append(os.path.abspath(filename))
                elif filename.endswith(".jpeg"):
                    jpeg_imgsx.append(filename)
        return

    # for dirnames in os.walk('/home/chris/PycharmProjects/TTA/app_images'):
    #     for dirname in dirnames:
    #         folders.append(dirname)




print("files for back ground " + str(background_img2x))
print("folders for back ground " + str(foldersx))

ImageBank()
print("AFTER files for back ground " + str(background_img2x))
print("AFTER folders for back ground " + str(foldersx))

