from os import walk

from PIL import Image
from rembg import remove


#this is a class to to remove unwnted background
 #from png files and save them
 #kept as coul;d be useful down the road
 #but as yet the outpot is stll showing a background

def convertImage():
    img = Image.open("./1.png")
    img = img.convert("RGBA")
    img2 = Image.open("./2.png")
    img2 = img2.convert("RGBA")
    
    
    die1 = Image.open("./1.png")
    die1 = die1.convert("RGBA")
    die2 = Image.open("./2.png")
    die2 = die2.convert("RGBA")
    die3 = Image.open("./3.png")
    die3 = die3.convert("RGBA")
    die4 = Image.open("./4.png")
    die4 = die4.convert("RGBA")
    die5 = Image.open("./5.png")
    die5 = die5.convert("RGBA")
    die6 = Image.open("./6.png")
    die6 = die6.convert("RGBA")

    di1 =remove(die1)
    di2 = remove(die2)
    di3 = remove(die3)
    di4 = remove(die4) 
    di5 = remove(die5)
    di6 = remove(die6)
    di1.save("./1v2.png")
    di2.save("./2v2.png")
    di3.save("./3v2.png")
    di4.save("./4v2.png")
    di5.save("./5v2.png")
    di6.save("./6v2.png")
    # die1 =
    # die2 =
    # die3 =
    # die4 = 
    # die5 =
    # die6 =



    datas = img.getdata()

    newData = []

    bluh_image = remove(img2)
    

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("./new2.png", "PNG")
    img2.save("./new3.png")

# def removeBackground():
#
#
# #
# #     ximg = Image
# #     for dirpath, dirnames, filenames in walk('/app_images/Dice_images'):
# #
# #         for filename in filenames:
# #             if filename.endswith(".png"):
# #                 str(filename) = Image.open("./1.png")
#
# bluh_image.save("./bluh.png")
print("Successful")



convertImage()
