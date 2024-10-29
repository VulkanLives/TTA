import subprocess
from tkinter import *
from tkinter import messagebox

import numpy as np
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkEntry
import pandas as pd

root = ctk.CTk()

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
root.geometry("500x250")

roll_count = 0
#gridx is a var for diplay purposes in roll fucntion
gridx = 1
first_activation = True
#list arraay to record the results
record = []
total_dice_rolled = 0



command_frame = ctk.CTkFrame(master=root, fg_color="khaki3", border_color="black")
command_frame.pack(side="top", fill="both", expand=True)

output_frame =  ctk.CTkFrame(master=root, fg_color="khaki3", border_color="black")
output_frame.pack(side="top", fill="both", expand=True)



res_frame = ctk.CTkFrame(master=output_frame, fg_color="khaki3", border_width=5, width=400, height=200,
                          border_color="black")
#user_input_frame = ctk.CTkFrame(master=command_frame, fg_color="khaki3", border_width=5, border_color="black")
user_input_frame = ctk.CTkFrame(master=command_frame, fg_color="khaki3", border_color="black")


#variable for check box options to determined and then actioned
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

#USER input boxes
presets = ["1", "5", "10", "15", "20"]
preset_option_box = ctk.CTkComboBox(user_input_frame, values=presets, state="readonly", width=75,font=("Helvetica", 18))
preset_option_box.grid(row=1, column=1, columnspan=2 )
preset_option_box.set("5")
custom_entry = ctk.CTkEntry(user_input_frame,width=75, font=("Helvetica", 18))
custom_entry.configure(state="disabled",fg_color="grey")
custom_entry.grid(row=2, column=1, columnspan=2)
user_input_frame.pack(side="left", fill="both", expand=False)

def user_input():
    global roll_count,first_activation

    #enable and disable "preset input box" and "custom user entry boox"
    if var1.get() == 1 :
        if roll_count >0:
            first_activation = False
        else:
            first_activation = True

    if var4.get() == 1:
        preset_option_box.configure(state="disabled")
        custom_entry.configure(state="normal", fg_color="white")
        custom_entry.focus()
    else:
        preset_option_box.configure(state="normal")
        custom_entry.configure(state="disabled",fg_color="grey")
    if var3.get() == 1:
        advanced_options()

# Create 3 checkboxes
checkbox_font = ctk.CTkFont(family='Helvetica',
                         size=12, weight='bold')
check1 = ctk.CTkCheckBox(user_input_frame, text="Show all rolls", variable=var1, onvalue=1, offvalue=0, font=checkbox_font, command=user_input)
check1.grid(row=1, column=3)

check2 = ctk.CTkCheckBox(user_input_frame, text="enable bar chart", variable=var2, onvalue=1, offvalue=0, font=checkbox_font)
check2.grid(row=1, column=4)

check3 = ctk.CTkCheckBox(user_input_frame, text="veiw array", variable=var3, onvalue=1, offvalue=0, font=checkbox_font, command=user_input)
check3.grid(row=2, column=3)

check4 = ctk.CTkCheckBox(user_input_frame, text="Enable user input", variable=var4, onvalue=1, offvalue=0, font =checkbox_font, command=user_input)
check4.grid(row=2, column=4)

check5 = ctk.CTkCheckBox(user_input_frame, text="show average", variable=var5, onvalue=1, offvalue=0,
                         font=checkbox_font)
check5.grid(row=3, column=3)


def show_roll_history():
    roll_history_win = ctk.CTkToplevel(root, fg_color="white")
    roll_history_win.title("Session Results")
    roll_history_win.geometry("400x200")
    roll_history_win.resizable(False, True)  # Width, He

    hist_frame =ctk.CTkFrame(master=roll_history_win, fg_color="khaki3", border_width=2, width=400, height=200,
                                            border_color="black")
    dice_lbl = ctk.CTkLabel(hist_frame, fg_color="khaki3", text='\u2680' + str(record))
    dice_lbl.pack()
    hist_frame.pack()
def advanced_options():
    print("total_dice_rolled = " +str(total_dice_rolled))
# def roll_count(num):
#     x = int(num)
#     click_count: int = +x
#     print(click_count)
#     roll_numpy()






def roll_numpy():
    global roll_count
    global gridx
    global first_activation, total_dice_rolled
    global df
   # res_frame.pack_forget()
    font_setup = ctk.CTkFont(family='Helvetica',
                             size=34, weight='bold')
    # Define different type of dice d6 = std di, d3 = 3 sides
    d6_sides = 6
    # n_rolls = int

    #roll_count = var to show all dice rolls using this var to alter what row eacg result is printed on
    print(roll_count)


    roll_count += 1
    print("roll count = " + str(roll_count))
    #if statement attempt at after clear button pressed rollr resulst are displayed
    # below most recent line of dice , but doesnt really work atm
    if var1.get() == 1 :
        if first_activation:
            gridx = roll_count
            print("gridx = "+ str(gridx))
        else:
            gridx = roll_count-1
    else:
        gridx = 1
        print("gridx =! " + str(gridx))

    # make sure of valid entry with "try" statement
    try:
       # if check4 == 1

        n_rolls = int(preset_option_box.get())
        test = []
        print("n_rolls = " + str(n_rolls))
        # Represent a die by using a numpy array
        die = np.array([i for i in range(1, d6_sides + 1)])
        rolls = np.array([np.random.choice(die) for _ in range(n_rolls)])
        #array/list below records the actual results
        record.append(rolls)
        test.append(rolls)
        total_dice_rolled +=n_rolls
        print(record)
        #print(record[roll_count-1])
       # print(test[roll_count - 1])
        print(record.__len__())

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
        first_activation =False
        pass
    except ValueError:
        messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window
def clr ():
    global roll_count, first_activation
    roll_count = 0
    first_activation = True
    res_frame.forget()
    print(df)

#below if statement can be expanded later to include other varations on result and roll types
#go_btn = ctk.CTkButton(master=user_input_frame, text="Roll", width=75, command= roll_numpy)
go_btn = ctk.CTkButton(master=user_input_frame, text="Roll", width=75, command= roll_numpy)

go_btn.grid(row=3, column=1)
clear_btn = ctk.CTkButton(master=user_input_frame, text="Clear", width= 75 , command= clr)
clear_btn.grid(row=4, column=1)
history_btn = ctk.CTkButton(master=user_input_frame, text="history", width= 75 , command= show_roll_history)
history_btn.grid(row=5, column=1)



root.mainloop()
