from random import random
import tkinter as tk
from tkinter import messagebox, Image, Menu
import customtkinter as ctk
from customtkinter import CTkFont
from classes import roll_dice as rd, imageBank as ib, detect_system as ds
from classes import numpy_roll_dice as nrd
from PIL import Image
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from classes.roll_dice import RollDice

ds.DetectSystem()

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
app = ctk.CTk()

#detect which OS/device is being used
os_name = ds.os_name


app.title("TableTop Allie")
app.geometry("800x600", )  # set starting window size
app.resizable(width=False, height=True)

result_array = []
bg_img_bank = []
img_index = int(0)
dice_img_path = ds.di_image_path


def load_image_bank():
    global bg_img_bank, img_index
    ib.ImageBank()
    bg_img_bank = ib.bg_image_bank
    x = int(ib.bg_image_bank.__len__())
    img_index = random.randint(0, x)
    print("from load_image_bank" + str(bg_img_bank.__len__()) + "image index = " + str(img_index))
    #return bg_img_bank, img_index
    return


def show_roll_order(s_order):
    dice_order = int(s_order)
    print(s_order)


top_frame = ctk.CTkFrame(master=app, fg_color="orange", border_width=2, border_color="black")
# note: the side=top makes the object stick highest point in the of the window when resizing whislt running
top_frame.pack(side="top", fill="both", expand=True)



bottom_frame = ctk.CTkFrame(master=app, fg_color="red", border_width=0, border_color="black")
bottom_frame.pack(side="top", fill="both", expand=True)



user_frame = ctk.CTkFrame(master=top_frame, fg_color="khaki3",border_width=2, border_color="black")
# note: the side=top makes the object stick highest point in the of the window when resizing whislt running

result_bx_one = ctk.CTkTextbox(master=user_frame, bg_color='white', width= 60, height= 60, border_width=2).grid(row=1, column=2)
result_bx_two = ctk.CTkTextbox(master=user_frame, bg_color='white', width= 60, height= 60, border_width=2).grid(row=2, column=2)
result_bx_three = ctk.CTkTextbox(master=user_frame, bg_color='white', width= 60, height= 60, border_width=2).grid(row=3, column=2)
result_bx_four = ctk.CTkTextbox(master=user_frame, bg_color='white', width= 60, height= 60, border_width=2).grid(row=4, column=2)
result_bx_five = ctk.CTkTextbox(master=user_frame, bg_color='white', width= 60, height= 60, border_width=2).grid(row=5, column=2)
result_bx_six = ctk.CTkTextbox(master=user_frame, bg_color='white', width= 60, height= 60, border_width=2).grid(row=6, column=2)

#result_bx_two = ctk.CTkLabel(master=user_frame, bg_color='white', text="",width=10).grid(row=2,column=2)
user_frame.pack(side="left", fill="both", expand=False)

frame3 = ctk.CTkFrame(master=bottom_frame, fg_color="orange", border_width=2, border_color="black")
frame3.pack()

def load_dice_images():
    die_one = ctk.CTkImage(Image.open(str(ds.di_image_path)+ "/1v2.png"), size=(75,75))
    die_two = ctk.CTkImage(Image.open(str(ds.di_image_path)+ "/2v2.png"), size=(75, 75))
    die_three = ctk.CTkImage(Image.open(str(ds.di_image_path)+ "/3v2.png"), size=(75,75))
    die_four = ctk.CTkImage(Image.open(str(ds.di_image_path)+ "/4v2.png"), size=(75, 75))
    die_five = ctk.CTkImage(Image.open(str(ds.di_image_path)+ "/5v2.png"), size=(75,75))
    die_six = ctk.CTkImage(Image.open(str(ds.di_image_path)+ "/6v2.png"), size=(75, 75))
    ctk.CTkLabel(master=user_frame, text="", image= die_one).grid(row=1,column=1)
    ctk.CTkLabel(master=user_frame, text="", image=die_two).grid(row=2,column=1)
    ctk.CTkLabel(master=user_frame, text="", image=die_three).grid(row=3,column=1)
    ctk.CTkLabel(master=user_frame, text="", image=die_four).grid(row=4,column=1)
    ctk.CTkLabel(master=user_frame, text="", image=die_five).grid(row=5,column=1)
    ctk.CTkLabel(master=user_frame, text="", image=die_six).grid(row=6,column=1)


load_dice_images()

result_frame = ctk.CTkFrame(master=top_frame, fg_color="yellow", border_width=2, width=200, height=200 , border_color="black")
result_frame.pack(side="right", fill="both", expand=True)
dice_order_frame = ctk.CTkFrame(master=top_frame)
dice_order_frame.pack(side="right", fill="both", expand=True)



e = ctk.CTkEntry(master=user_frame, border_width=1)
e.grid(row=1, column= 4, padx= 20)

def roll_numpy(event=None):
    # Define different type of dice d6 = std di, d3 = 3 sides
    d6_sides = 6
    d3_sides = 3
    n_rolls = int
    try:
        #make sure of valid entry
        n_rolls= int(e.get())
        pass
    except ValueError:
        messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window
        e.delete(0, 'end')  # clear entry box
        e.focus()  # make cursor active in entry box
    print("n_rolls = " + str(n_rolls))
    # Represent a die by using a numpy array
    die = np.array([i for i in range(1, d6_sides + 1)])
    rolls = np.array([np.random.choice(die) for _ in range(n_rolls)])
    display_numpy_result(rolls)
    print(rolls)
    #work out mean and variance
    print(f"mean of first_rolls: {np.mean(rolls):.2f}\nvariance of first_rolls: {np.var(rolls):.2f}\n")


def roll(event=None):
    global result_array
    try:
        int(e.get())
        x = e.get()
        print("x = " + str(x))
        print(x)
        rd.RollDice(x)
        print()
        result_array = rd.occurance_list
        sequence_array = rd.roll_order
        pass
    except ValueError:
        messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window
        e.delete(0, 'end')  # clear entry box
        e.focus()  # make cursor active in entry box
    #display_result(result_array)

def display_numpy_result(rolls):
    print(rolls)
    roll_result = []
    roll_result = np.array(rolls)
    print("roll result = " + str(roll_result))
    helv36 = CTkFont(family='Helvetica',
                         size=36, weight='bold')
    #
    ctk.CTkLabel(master=user_frame, bg_color='white', text=str(np.count_nonzero(rolls == 1)),font=helv36).grid(row=1, column=2)
    ctk.CTkLabel(master=user_frame, bg_color='white',  text=str(np.count_nonzero(rolls == 2)),font=helv36).grid(row=2, column=2)
    ctk.CTkLabel(master=user_frame, bg_color='white',  text=str(np.count_nonzero(rolls == 3)),font=helv36).grid(row=3, column=2)
    ctk.CTkLabel(master=user_frame, bg_color='white', text=str(np.count_nonzero(rolls == 4)),font=helv36).grid(row=4, column=2)
    ctk.CTkLabel(master=user_frame, bg_color='white',  text=str(np.count_nonzero(rolls == 5)),font=helv36).grid(row=5, column=2)
    ctk.CTkLabel(master=user_frame, bg_color='white',  text=str(np.count_nonzero(rolls == 6)),font=helv36).grid(row=6, column=2)
    #
    # ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=2, column=3)
    # ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=3, column=3)
    # ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=4, column=3)
    # ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=5, column=3)
    # ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=6, column=3)

def display_result(res_array):
    global result_bx_two
    #this commented blocked texual dice which i quite liked and wanted t omaybe keep for something elese
    # ctk.CTkLabel(master=user_frame, fg_color="white", width=1, text='\u2680' + str(res_array[0])).pack(padx=15,
    #                                                                                            side='left')
    # ctk.CTkLabel(master=user_frame, fg_color="white", text='\u2681' + str(res_array[1])).pack(padx=15, side='left')
    # ctk.CTkLabel(master=user_frame, fg_color="white", text="\u2682 = " + str(res_array[2])).pack(padx=15, side='left')
    # ctk.CTkLabel(master=user_frame, fg_color="white", text="\u2683 = " + str(res_array[3])).pack(padx=15, side='left')
    # ctk.CTkLabel(master=user_frame, fg_color="whit7e", text="\u2684 = " + str(res_array[4])).pack(padx=15, side='left')
    # ctk.CTkLabel(master=user_frame, fg_color="white", text="\u2685" + str(res_array[5])).pack(padx=15, side='left')
    helv36 = CTkFont(family='Helvetica',
                         size=36, weight='bold')

    ctk.CTkLabel(master=user_frame, text=str(res_array[0]),font=helv36).grid(row=1, column=2)
    ctk.CTkLabel(master=user_frame,  text=str(res_array[1]),font=helv36).grid(row=2, column=2)
    ctk.CTkLabel(master=user_frame,  text=str(res_array[2]),font=helv36).grid(row=3, column=2)
    ctk.CTkLabel(master=user_frame,  text=str(res_array[3]),font=helv36).grid(row=4, column=2)
    ctk.CTkLabel(master=user_frame,  text=str(res_array[4]),font=helv36).grid(row=5, column=2)
    ctk.CTkLabel(master=user_frame,  text=str(res_array[5]),font=helv36).grid(row=6, column=2)

    ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=2, column=3)
    ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=3, column=3)
    ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=4, column=3)
    ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=5, column=3)
    ctk.CTkLabel(master=user_frame, text="   ",font=helv36).grid(row=6, column=3)

def dice_results_in_order():
    global result_list
    dice_order_frame.grid(row=15, column=4)

# call load image function, only background active atm
load_image_bank()

roll_btn = ctk.CTkButton(master=user_frame, text="Roll Dice",command=roll)# "command" makes the calls the above function, fg is text colour "foreground" and Bg = background
roll_btn.grid(row= 3, column= 4)
numppy_roll_btn = ctk.CTkButton(master=user_frame, text="Roll Numpy Dice",command=roll_numpy)# "command" makes the calls the above function, fg is text colour "foreground" and Bg = background
numppy_roll_btn.grid(row= 4, column= 4)
button_quit = ctk.CTkButton(master=user_frame, text="Exit", command=app.quit)
button_quit.grid(row= 9, column= 5)

#create var for Menu
my_menu = tk.Menu(app)
# Create a category item  menu
file_menu = tk.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
# Add sub-items to File_Menu
file_menu.add_separator()
# Add sub-items to File_Menu
file_menu.add_command(label="Exit", command=app.quit)

edit_menu: Menu = tk.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)
# Add sub item to edit menu
#edit_menu.add_command(label="results")
edit_menu.add_command(label="preferences")
sub_edit_menu = Menu(edit_menu, tearoff= False)
edit_menu.add_cascade(label = 'Results', menu=sub_edit_menu)

results_menu = Menu(sub_edit_menu,tearoff= False)
results_menu.add_cascade(label = 'Show dice order', menu=results_menu)
results_menu.add_checkbutton(label="show dice in order", command=lambda: show_roll_order(True))

#results_menu.add_cascade(label="show dice in order", menu= sub_edit_menu)
#results_menu.add_checkbutton(label="show dice in order", command=lambda: show_roll_order(True))


app.config(menu=my_menu)

#open an image at random from my Image bank class and display
bg_img = ctk.CTkImage(light_image=Image.open(str(bg_img_bank[img_index-1])),dark_image=Image.open((str(bg_img_bank[img_index-1]))),size=(300,300)) # WidthxHeight
bg_label = ctk.CTkLabel(master=result_frame, text="", image=bg_img)
bg_label.pack()

e.focus()

app.mainloop()