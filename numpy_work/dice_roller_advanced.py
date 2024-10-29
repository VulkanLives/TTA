import subprocess
from tkinter import *
from tkinter import messagebox

import numpy as np
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkEntry

root = ctk.CTk()

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
root.geometry("300x300")

main_frame = ctk.CTkFrame(master=root, fg_color="khaki3", border_width=2, border_color="black")

roll_count = 0




# note: the side=top makes the object stick highest point in the of the window when resizing whislt running


def dice_win():
    dice_window = ctk.CTkToplevel(root, fg_color="white")
    dice_window.title("Dice Roller with numpy")
    dice_window.geometry("400x200")
    dice_window.resizable(True, True)  # Width, Height
    res_frame = ctk.CTkFrame(master=dice_window, fg_color="khaki3", border_width=2, width=400, height=200,
                             border_color="black")
    dw_frame = ctk.CTkFrame(master=dice_window, fg_color="khaki3", border_width=2, width=400, height=200,
                            border_color="black")
    presets = ["1", "5", "10", "15", "20"]
    preset_option_box = ctk.CTkComboBox(dw_frame, values=presets, state="readonly", width=75, font=("Helvetica", 18))
    preset_option_box.grid(row=1, column=1)
    preset_option_box.set("5")
    custom_entry = ctk.CTkEntry(dw_frame,width=100, font=("Helvetica", 18))

    def user_input():
        #enable and disable "preset input box"
        print("hello")
        if var4.get() == 1:
            preset_option_box.configure(state="disabled")
            custom_entry.grid(row=1, column=1)
        else:
            preset_option_box.configure(state="normal")


    # Create 3 checkboxes
    check1 = ctk.CTkCheckBox(dw_frame, text="Show all rolls", variable=var1, onvalue=1, offvalue=0, font=("Helvetica", 12))
    check1.grid(row=1, column=3)

    check2 = ctk.CTkCheckBox(dw_frame, text="enable bar chart option", variable=var2, onvalue=1, offvalue=0, font=("Helvetica", 12))
    check2.grid(row=1, column=4)

    check3 = ctk.CTkCheckBox(dw_frame, text="show rolls above (x)", variable=var3, onvalue=1, offvalue=0, font=("Helvetica", 12))
    check3.grid(row=2, column=4)

    check4 = ctk.CTkCheckBox(dw_frame, text="custom number of rolls", variable=var4, onvalue=1, offvalue=0, font=("Helvetica", 12), command=user_input)
    check4.grid(row=2, column=3)

    check5 = ctk.CTkCheckBox(dw_frame, text="show average", variable=var5, onvalue=1, offvalue=0,
                             font=("Helvetica", 12))
    check5.grid(row=3, column=4)

    # # Create a button
    # my_button = Button(dw_frame, text="Submit", command=clicked)
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
       # res_frame.pack_forget()
        font_setup = ctk.CTkFont(family='Helvetica',
                                 size=34, weight='bold')
        # Define different type of dice d6 = std di, d3 = 3 sides
        d6_sides = 6
        d3_sides = 3
        # n_rolls = int

        #roll_count = var to show all dice rolls using this var to alter what row eacg result is printed on
        roll_count += 1
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
            print(rolls)
            # work out mean and variance
            print(f"mean of first_rolls: {np.mean(rolls):.2f}\nvariance of first_rolls: {np.var(rolls):.2f}\n")
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='\u2680' + str(np.count_nonzero(rolls == 1)),
                         font=font_setup).grid(row= int(gridx), column= 1)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= int(1), column= 2)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='\u2681' + str(np.count_nonzero(rolls == 2)),
                         font=font_setup).grid(row= int(gridx), column= 3)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= int(gridx), column= 4)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2682" + str(np.count_nonzero(rolls == 3)),
                         font=font_setup).grid(row= int(gridx), column= 5)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= int(gridx), column= 6)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2683" + str(np.count_nonzero(rolls == 4)),
                         font=font_setup).grid(row= int(gridx), column= 7)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= int(gridx), column= 8)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2684" + str(np.count_nonzero(rolls == 5)),
                         font=font_setup).grid(row= int(gridx), column= 9)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= int(gridx), column= 10)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2685" + str(np.count_nonzero(rolls == 6)),
                         font=font_setup).grid(row= int(gridx), column= 11)
            #ctk.CTkLabel(master=res_frame, text=str(np.count_nonzero(rolls ==1)), font=font_setup).pack(side='left')

            res_frame.pack(pady=20)
            pass
        except ValueError:
            messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window
    def clr ():
        global roll_count
        res_frame.forget()
        roll_count = 0
#below if statement can be expanded later to include other varations on result and roll types
    dice_window.title("Dice Roller Lite - NumPy Edition")
    go_btn = ctk.CTkButton(master=dw_frame, text="Roll", width=75, command= roll_numpy)
    go_btn.grid(row=2, column=1)
    clear_btn = ctk.CTkButton(master=dw_frame, text="Clear", width= 75 , command= clr)
    clear_btn.grid(row=3, column=1)

    # menu options for window

    # create var for Menu
    my_menu = tk.Menu(dice_window)
    # Create a category item  menu
    file_menu = tk.Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    # Add sub-items to File_Menu
    file_menu.add_separator()
    # Add sub-items to File_Menu
    file_menu.add_command(label="Exit", command=root.quit)

    edit_menu: tk.Menu = tk.Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    # Add sub item to edit menu
    # edit_menu.add_command(label="results")
    edit_menu.add_command(label="preferences")
    sub_edit_menu = tk.Menu(edit_menu, tearoff=False)
    edit_menu.add_cascade(label='Use advanced options', menu=sub_edit_menu)
    results_menu = tk.Menu(sub_edit_menu, tearoff=False)
    results_menu.add_cascade(label='Show dice order', menu=sub_edit_menu)
    edit_menu.add_checkbutton(label="show advanced option on screen", command=advanced_options("show_sequence"))

    dw_frame.pack()
    dice_window.config(menu=my_menu)

    # r_label.config(text=preset_option_box.get())

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
rolldice_numpy_btn = ctk.CTkButton(master=main_frame, text="Roll Dice w/ Numpy", command=dice_win).pack(pady=5)
main_frame.pack(side="top", fill="both", expand=True)

root.mainloop()
