from tkinter import *
from tkinter import messagebox
import tkinter as tk
import customtkinter as ctk
from classes import roll_dice as rd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

root = ctk.CTk()

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
root.geometry("300x200")

program_lib = []
# show_roll_sequence = False


main_frame = ctk.CTkFrame(master=root, fg_color="khaki3", border_width=2, border_color="black")



# note: the side=top makes the object stick highest point in the of the window when resizing whislt running

def todo_list():
    todo_window = ctk.CTkToplevel(root, fg_color="white")
    todo_window.title("tasks done that need to added")
    todo_window.geometry("400x200")
    todo_window.resizable(False, True)  # Width, Height
    done_btn = ctk.CTkButton(master=todo_window, text="done", width=100)
    done_btn.grid(row=2, column=1)
    todo_btn = ctk.CTkButton(master=todo_window, text="Need to do", width=100)
    todo_btn.grid(row=3, column=1)




def new():
    new_window = ctk.CTkToplevel(root, fg_color="white")
    new_window.title("This is a new window!")
    new_window.geometry("400x200")
    new_window.resizable(False, True)  # Width, Height

    def close():
        new_window.destroy()
        new_window.update()


def dice_win(meth_choice):
    method_choice = meth_choice

    dice_window = ctk.CTkToplevel(root, fg_color="white")
    dice_window.title("Dice Roller Lite")
    dice_window.geometry("400x200")
    dice_window.resizable(True, True)  # Width, Height
    res_frame = ctk.CTkFrame(master=dice_window, fg_color="khaki3", border_width=2, width=400, height=200,
                             border_color="black")
    dw_frame = ctk.CTkFrame(master=dice_window, fg_color="khaki3", border_width=2, width=400, height=200,
                            border_color="black")
    presets = ["1", "5", "10", "15", "20"]
    preset_option_box = ctk.CTkComboBox(dw_frame, values=presets, state="readonly", width=100, font=("Helvetica", 18))
    preset_option_box.grid(row=1, column=1)
    preset_option_box.set("5")

    def roll_it():
        x = preset_option_box.get()
        font_setup = ctk.CTkFont(family='Helvetica',
                                 size=24, weight='bold')
        try:

            rd.RollDice(x)
            result_list = rd.occurance_list
            sequence_list: list[int] = rd.roll_order
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='\u2680' + str(result_list[0]),
                         font=font_setup).pack(padx=15,
                                               side='left')
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='\u2681' + str(result_list[1]),
                         font=font_setup).pack(padx=15, side='left')
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2682 = " + str(result_list[2]),
                         font=font_setup).pack(padx=15, side='left')
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2683 = " + str(result_list[3]),
                         font=font_setup).pack(padx=15, side='left')
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2684 = " + str(result_list[4]),
                         font=font_setup).pack(padx=15, side='left')
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2685" + str(result_list[5]),
                         font=font_setup).pack(padx=15, side='left')
            ctk.CTkLabel(master=res_frame, text=str(result_list[0]), font=font_setup).pack(side='left')

            pass
        except ValueError:
            messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window

        res_frame.pack()

    def advanced_options(option):
        opt = option
        print(opt)

    def roll_numpy():
       # res_frame.pack_forget()
        font_setup = ctk.CTkFont(family='Helvetica',
                                 size=34, weight='bold')
        # Define different type of dice d6 = std di, d3 = 3 sides
        d6_sides = 6
        d3_sides = 3
        # n_rolls = int
        try:
            # make sure of valid entry
            n_rolls = int(preset_option_box.get())
            face_count = []

            print("n_rolls = " + str(n_rolls))
            # Represent a die by using a numpy array
            die = np.array([i for i in range(1, d6_sides + 1)])
            rolls = np.array([np.random.choice(die) for _ in range(n_rolls)])
            print(rolls)
            # work out mean and variance
            print(f"mean of first_rolls: {np.mean(rolls):.2f}\nvariance of first_rolls: {np.var(rolls):.2f}\n")
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='\u2680' + str(np.count_nonzero(rolls == 1)),
                         font=font_setup).grid(row= 1, column= 1)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= 1, column= 2)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='\u2681' + str(np.count_nonzero(rolls == 2)),
                         font=font_setup).grid(row= 1, column= 3)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= 1, column= 4)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2682" + str(np.count_nonzero(rolls == 3)),
                         font=font_setup).grid(row= 1, column= 5)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= 1, column= 6)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2683" + str(np.count_nonzero(rolls == 4)),
                         font=font_setup).grid(row= 1, column= 7)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= 1, column= 8)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2684" + str(np.count_nonzero(rolls == 5)),
                         font=font_setup).grid(row= 1, column= 9)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text='  ',
                         font=font_setup).grid(row= 1, column= 10)
            ctk.CTkLabel(master=res_frame, fg_color="khaki3", text="\u2685" + str(np.count_nonzero(rolls == 6)),
                         font=font_setup).grid(row= 1, column= 11)
            #ctk.CTkLabel(master=res_frame, text=str(np.count_nonzero(rolls ==1)), font=font_setup).pack(side='left')
            res_frame.pack(pady=20)
            pass
        except ValueError:
            messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window

#below if statement can be expanded later to include other varations on result and roll types
    if method_choice == "roll_it":
        go_btn = ctk.CTkButton(master=dw_frame, text="Roll", width=100, command=roll_it)
        go_btn.grid(row=2, column=1)

    elif method_choice == "roll_numpy":
        dice_window.title("Dice Roller Lite - NumPy Edition")
        go_btn = ctk.CTkButton(master=dw_frame, text="Roll", width=100, command=roll_numpy)
        go_btn.grid(row=2, column=1)

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

    edit_menu: Menu = tk.Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    # Add sub item to edit menu
    # edit_menu.add_command(label="results")
    edit_menu.add_command(label="preferences")
    sub_edit_menu = Menu(edit_menu, tearoff=False)
    edit_menu.add_cascade(label='Use advanced options', menu=sub_edit_menu)
    results_menu = Menu(sub_edit_menu, tearoff=False)
    results_menu.add_cascade(label='Show dice order', menu=sub_edit_menu)
    edit_menu.add_checkbutton(label="show advanced option on screen", command=advanced_options("show_sequence"))

    dw_frame.pack(fill=X)
    dice_window.config(menu=my_menu)

    # r_label.config(text=preset_option_box.get())


my_button = ctk.CTkButton(main_frame, text="Open New Window", command=new)
my_button.pack(pady=5)
rolldice_lite_btn = ctk.CTkButton(master=main_frame, text="Roll Dice Lite", command=lambda :dice_win("roll_it"))
rolldice_lite_btn.pack(pady=5)
rolldice_numpy_btn = ctk.CTkButton(master=main_frame, text="Roll Dice w/ Numpy", command=lambda :dice_win("roll_numpy")).pack(pady=5)
todo_list = ctk.CTkButton(master=main_frame, text="To Do list", command=todo_list).pack(pady=5)
image_work_btn = ctk.CTkButton(master=main_frame, text="Image Work").pack(pady=5)
detect_system_btn = ctk.CTkButton(master=main_frame, text="System Detection").pack(pady=5)

# rolldice_lite_btn = ctk.CTkButton(master=btn_frame, text="Roll Dice Lite")
main_frame.pack(side="top", fill="both", expand=True)

root.mainloop()


