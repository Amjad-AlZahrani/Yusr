
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, IntVar, Radiobutton
from tkinter import messagebox

import pygame

from scores import addScore2, center_window
from findScore import printScore2, clear, clear1, clear2, clear3

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\YusrGP\YusrProject\assets\frame29")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_FinishSectionTwoPage():
    file_to_run_path = r"C:\YusrGP\YusrProject\FinishSectionTwoPage.py"
    window.destroy()
    subprocess.run(["python", file_to_run_path], check=True)
    #window.destroy() # Close the current window
    #import FinishSectionTwoPage.py

def open_HomePage():
    clear()
    clear1()
    clear2()
    clear3()
    file_to_run_path = r"C:\YusrGP\YusrProject\HomePage.py"
    window.destroy()
    subprocess.run(["python", file_to_run_path], check=True)
    #window.destroy() # Close the current window
    #import HomePage.py

window = Tk()
window.title('Game')

window.geometry("396x688")
window.configure(bg = "#FFEDED")


canvas = Canvas(
    window,
    bg = "#FFEDED",
    height = 688,
    width = 396,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    198.0,
    628.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    198.0,
    112.0,
    image=image_image_2
)

pygame.init()
def perform_action(event):
    sound = pygame.mixer.Sound(r"C:\YusrGP\YusrProject\assets\frame29\Game6.mp3")
    sound.play()
canvas.tag_bind(image_2, "<Button-1>", perform_action)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    198.0,
    404.0,
    image=image_image_3
)
#Radio_button
radio_var1 = IntVar()
radio_var2 = IntVar()
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Radiobutton(
    image=button_image_4,
    indicatoron=0,
    borderwidth=0,
    highlightthickness=0,
    variable=radio_var1,
    value=1,
)
button_4.place(
    x=60.0,
    y=284.0,
    width=90.0,
    height=90.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Radiobutton(
    image=button_image_2,
    indicatoron=0,
    borderwidth=0,
    highlightthickness=0,
    variable=radio_var1,
    value=2,
)
button_2.place(
    x=153.0,
    y=284.0,
    width=90.0,
    height=92.0
)
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Radiobutton(
    image=button_image_6,
    indicatoron=0,
    borderwidth=0,
    highlightthickness=0,
    variable=radio_var1,
    value=3,
)
button_6.place(
    x=247.0,
    y=284.0,
    width=90.0,
    height=90.0
)

#group2
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Radiobutton(
    image=button_image_1,
    indicatoron=0,
    borderwidth=0,
    highlightthickness=0,
    variable=radio_var2,
    value=1,
)
button_1.place(
    x=59.0,
    y=461.0,
    width=88.0,
    height=88.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Radiobutton(
    image=button_image_7,
    indicatoron=0,
    borderwidth=0,
    highlightthickness=0,
    variable=radio_var2,
    value=2,
)
button_7.place(
    x=153.0,
    y=459.0,
    width=90.0,
    height=91.0
)
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Radiobutton(
    image=button_image_5,
    indicatoron=0,
    borderwidth=0,
    highlightthickness=0,
    variable=radio_var2,
    value=3,
)
button_5.place(
    x=247.0,
    y=460.0,
    width=90.0,
    height=89.0
)


def open_page_two():
    if radio_var1.get() and radio_var2.get():
        score6 = 0 
        if radio_var1.get()  == 1:
            score6 += 3
        if radio_var1.get() == 2:
            score6 += 3
        if radio_var2.get()  == 2:
            score6 += 3
        if radio_var2.get()  == 3:
            score6 += 3
        addScore2(score6)
        printScore2()
        file_to_run_path = r"C:\YusrGP\YusrProject\FinishSectionTwoPage.py"
        window.destroy()
        subprocess.run(["python", file_to_run_path], check=True)
    else:
       messagebox.showwarning(title="تنبيه", message="اختر ليتم نقلك للصفحة التالية")

#next_booton
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_page_two,
    relief="flat"
)
button_3.place(
    x=153.0,
    y=579.0,
    width=90.0,
    height=61.875
)

button_home_2 = PhotoImage(
    file=relative_to_assets("homeButton.png"))
home_2 = Button(
    image=button_home_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_HomePage,
    relief="flat"
)
home_2.place(
    x=307.0,
    y=19.0,
    width=60.05078125,
    height=51.6392822265625
)

window.resizable(False, False)
center_window(window)
window.mainloop()
