import os

back_imgs = []
#look through the foler specified for png files.
# why do this? instead of just writing them into an array myself?
#should allow me to copy a paste new pic into folders an dit will pick them up
#could probably do it by using python to add file then saving the path but that will be later down the the line

for dirpath, dirnames, filenames in os.walk('/app_images/backgrounds'):
   for filename in filenames:
        if filename.endswith(".png"):
            bg_array.append(os.path.abspath(os.path.join(dirpath, filename)))

print(bg_array)
print(bg_array)





# class ImageBank:
#
#     print("Listing Python file:")
#     for dirpath, dirnames, filenames in os.walk("."):
#         for filename in filenames:
#             if filename.endswith(".png"):
#                 pngFiles.append(filename)
#        # for dirname in dirnames in os.walk("/background"):
#            # print("yes" + str(dirname))
#         for name in dirnames:
#             folders.append(name)


