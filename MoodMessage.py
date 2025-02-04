# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from scores import center_window

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\YusrGP\YusrProject\assets\frame22")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_SectionTwoPage():
    file_to_run_path = r"C:\YusrGP\YusrProject\SectionTwoPage.py"
    window.destroy()
    subprocess.run(["python", file_to_run_path], check=True)
    #window.destroy() # Close the current window
    #import SectionTwoPage.py


window = Tk()
window.title('Mood')

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
    204.0,
    646.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    198.0,
    621.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    198.0,
    320.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    284.0,
    252.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    113.0,
    399.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    113.0,
    252.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    284.0,
    399.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    196.0,
    100.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    195.0,
    535.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    204.0,
    341.0,
    image=image_image_10
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_SectionTwoPage,
    relief="flat"
)
button_1.place(
    x=155.0,
    y=429.0,
    width=85.80224609375,
    height=58.30084228515625
)
window.resizable(False, False)
center_window(window)
window.mainloop()