
from tkinter import *
from tkinter import messagebox

import numpy as np
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkFrame

root = ctk.CTk()

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
root.geometry("420x150")
root.resizable(True, True)
#numpy_dice_main = CTkFrame(master=root,fg_color="khaki3", border_width=2, border_color="black")

roll_count = 0
historic_count = 0
roll_history = []
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

  # Width, Height
dice_window =ctk.CTkFrame(root, fg_color="khaki3", border_width=2, width=420, height=150,
                         border_color="black")
res_frame = ctk.CTkFrame(master=dice_window, fg_color="khaki3", border_width=2, width= 420, height=150,
                         border_color="black")
dw_frame = ctk.CTkFrame(master=res_frame, fg_color="khaki3", border_width=2, width=420, height=150,
                         border_color="black")
presets = ["1", "5", "10", "15", "20"]
custom_entry = ctk.CTkEntry(dice_window,border_width=2 ,width=75, font=("Helvetica", 18),fg_color="grey",border_color="black")
preset_option_box = ctk.CTkComboBox(dice_window, values=presets, state="readonly",border_width=1, width=75, font=("Helvetica", 18))
preset_option_box.grid(row=1, column=1, columnspan= 2)
preset_option_box.set("5")
custom_entry.configure(state="disabled")
custom_entry.grid(row=2, column=1)


def user_input():
    #enable and disable "preset input box"
    print("hello")
    if var4.get() == 1:
        custom_entry.configure(state="normal",fg_color="white")
        preset_option_box.configure(state="disabled")
        custom_entry.focus()

    else:
        preset_option_box.configure(state="normal")
        custom_entry.configure(state="disabled",fg_color="grey")


# Create 3 checkboxes
check1 = ctk.CTkCheckBox(dice_window, text="Show all rolls", variable=var1, onvalue=1, offvalue=0, font=("Helvetica", 12))
check1.grid(row=1, column=3)

check2 = ctk.CTkCheckBox(dice_window, text="enable bar chart option", variable=var2, onvalue=1, offvalue=0, font=("Helvetica", 12))
check2.grid(row=1, column=4)

check3 = ctk.CTkCheckBox(dice_window, text="show rolls above (x)", variable=var3, onvalue=1, offvalue=0, font=("Helvetica", 12))
check3.grid(row=2, column=4)

check4 = ctk.CTkCheckBox(dice_window, text="custom number of rolls", variable=var4, onvalue=1, offvalue=0, font=("Helvetica", 12), command=user_input)
check4.grid(row=2, column=3)

check5 = ctk.CTkCheckBox(dice_window, text="show average", variable=var5, onvalue=1, offvalue=0,
                         font=("Helvetica", 12))
check5.grid(row=3, column=4)



# # Create a button
# my_button = Button(dice_window, text="Submit", command=clicked)
# my_button.pack(pady=20)

def advanced_options(option):
    opt = option
    print(opt)

# def roll_count(num):
#     x = int(num)
#     click_count: int = +x
#     print(click_count)
#     roll_numpy()

def roll_numpy():
    global roll_count
    global historic_count
   # res_frame.pack_forget()
    font_setup = ctk.CTkFont(family='Helvetica',
                             size=34, weight='bold')
    # Define different type of dice d6 = std di, d3 = 3 sides
    d6_sides = 6
    d3_sides = 3
    # n_rolls = int

    #roll_count = var to show all dice rolls using this var to alter what row eacg result is printed on
    roll_count += 1
    historic_count += 1
    print("roll count = " + str(roll_count))
    #if statement attempt at after clear button pressed rollr resulst are displayed
    # below most recent line of dice , but doesnt really work atm
    if var1.get() == 1:
        gridx = roll_count
        print("gridx =! "+ str(gridx))
    else:
        gridx = 1
        print("gridx =! " + str(gridx))

    # make sure of valid entry with "try" statement
    try:
       # if check4 == 1

        n_rolls = int(preset_option_box.get())

        print("n_rolls = " + str(n_rolls))
        # Represent a die by using a numpy array
        die = np.array([i for i in range(1, d6_sides + 1)])
        rolls = np.array([np.random.choice(die) for _ in range(n_rolls)])
       # roll_history[int(historic_count-1)] =rolls
        
        print(rolls)
        # work out mean and variance
        print(f"mean of first_rolls: {np.mean(rolls):.2f}\nvariance of first_rolls: {np.var(rolls):.2f}\n")
        ctk.CTkLabel(master=dw_frame, fg_color="khaki3", text='\u2680' + str(np.count_nonzero(rolls == 1)),
                     font=font_setup).grid(row= int(gridx), column= 1)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
        #              font=font_setup).grid(row= int(1), column= 2)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='\u2681' + str(np.count_nonzero(rolls == 2)),
        #              font=font_setup).grid(row= int(gridx), column= 3)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
        #              font=font_setup).grid(row= int(gridx), column= 4)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2682" + str(np.count_nonzero(rolls == 3)),
        #              font=font_setup).grid(row= int(gridx), column= 5)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
        #              font=font_setup).grid(row= int(gridx), column= 6)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2683" + str(np.count_nonzero(rolls == 4)),
        #              font=font_setup).grid(row= int(gridx), column= 7)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
        #              font=font_setup).grid(row= int(gridx), column= 8)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2684" + str(np.count_nonzero(rolls == 5)),
        #              font=font_setup).grid(row= int(gridx), column= 9)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
        #              font=font_setup).grid(row= int(gridx), column= 10)
        # ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2685" + str(np.count_nonzero(rolls == 6)),
        #              font=font_setup).grid(row= int(gridx), column= 11)
        # #ctk.CTkLabel(master=res_frame, text=str(np.count_nonzero(rolls ==1)), font=font_setup).pack(side='left')

        res_frame.pack(pady=20)
        pass
    except ValueError:
        messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window
def clr ():
    global roll_count
    res_frame.forget()
    roll_count = 0
#below if statement can be expanded later to include other varations on result and roll types
go_btn = ctk.CTkButton(master=dice_window, text="Roll", width=75, command= roll_numpy)
go_btn.grid(row=3, column=1)
clear_btn = ctk.CTkButton(master=dice_window, text="Clear", width= 75 , command= clr)
clear_btn.grid(row=4, column=1)

dice_window.pack()
# menu options for window


root.mainloop()

