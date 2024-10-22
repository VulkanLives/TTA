import platform

os_name = platform.system()
ipath = ""
all_img = ["", ""]
project_path = ""
di_image_path = ""

class DetectSystem:

    def __init__(self):
        global  ipath, project_path,all_img, di_image_path
        self.project_path = project_path
        self.os_name = os_name
        self.ipath = ipath
        self.all_img = all_img
        self.di_image_path = di_image_path
        if os_name == "Windows":
            ipath = 'C:/Users/creid/PycharmProjects/TTA/classes/app_images/backgrounds/'
            di_image_path = 'C:/Users/creid/PycharmProjects/TTA/classes/app_images/Dice_images/'
            all_img = ["bg" + 'C:/Users/creid/PycharmProjects/TTA/classes/app_images/backgrounds/']
            project_path = 'C:/Users/creid/PycharmProjects/TTA/'
            print("Windows system detected")
        elif os_name == "Linux":
            ipath  = '/home/chris/PycharmProjects/TTA/app_images/backgrounds/'
            di_image_path = '/home/chris/PycharmProjects/TTA/app_images/Dice_images'
            all_img = ["bg"+'/home/chris/PycharmProjects/TTA/app_images/backgrounds/']
            project_path = '/'

            print("Linux system detected")
        elif os_name == "Android":
            print('android detected')
            ipath  = '/storage/emulated/0/Documents/Python/app_images/backgrounds/'
            di_image_path = '/storage/emulated/0/Documents/Python/app_images/Dice_images/'
            project_path = '/storage/emulated/0/Documents/Python/'
        return
DetectSystem()
print(ipath)
print(all_img[0])