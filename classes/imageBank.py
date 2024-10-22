import os
from os import path, walk
import platform
import sys
import re
#from detect_system import DetectSystem
import classes.detect_system as ds
ds.DetectSystem()

joke_path = []
# '/home/chris/PycharmProjects/TTA/app_images/jokes'
folders = []
pngFilesx = []
bg_image_bank = []
meme_imagesx = []
dice_imgx = []
jpeg_imgsx = []
img_path = ds.ipath
di_path = ds.di_image_path
testpath = '/home/chris/PycharmProjects/TTA/app_images'


class ImageBank:

    def __init__(self) -> None:
        # self. = []
        self.pngFilesx = pngFilesx
       # self. =
        self.bg_image_bank = bg_image_bank
        self.meme_images = meme_imagesx
        self.dice_img = dice_imgx
        self.jpeg_imgs = jpeg_imgsx
        self.img_path = img_path
        self.testpath = testpath

        print("os dot walk dirs "+str(os.walk(testpath)))

        for dirpath, dirnames, filenames in walk(str(img_path)):

            for filename in filenames:
                if filename.endswith(".png"):
                    pngFilesx.append(filename)
                    bg_image_bank.append(path.join(dirpath, filename))
                elif filename.endswith(".jpeg"):
                    jpeg_imgsx.append(filename)

       # for dirpath, dirnames, filenames in walk(str(testpath)):
        for dirpath, dirnames, filenames in walk(str(testpath)+"/jokes"):
            for filename in filenames:
                if filename.endswith(".png"):
                    pngFilesx.append(filename)
                    meme_imagesx.append(path.join(dirpath, filename))

        for dirpath, dirnames, filenames in walk(str(testpath)+"/Dice_images"):
            for filename in filenames:
                dice_imgx.append(filename)



ImageBank()

#below code is a reminder to do the above neater and use then use loop and array to
#load images to correct folder
# subfolders = [ f.path for f in os.scandir(testpath) if f.is_dir() ]
# print(subfolders)
# print(dice_imgx)