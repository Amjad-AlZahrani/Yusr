import tkinter as tk
from tkinter import messagebox
from pathlib import Path



OUTPUT_PATH = Path(__file__).parent
path = r"C:\YusrGP\YusrProject\assets\message"

ASSETS_PATH = OUTPUT_PATH / Path(path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def custom_messagebox(title, message, message_type):
    root = tk.Tk()
    root.withdraw() 

    if message_type == "error":
        icon = tk.PhotoImage(file=relative_to_assets("error.png"))  
    elif message_type == "success":
        icon = tk.PhotoImage(file=relative_to_assets("right.png")) 
    else:
        icon = None

    if icon:
        root.tk.call('wm', 'iconbitmap', root._w, icon)

    result = messagebox.showinfo(title, message)

    root.destroy()  

# # Example usage:
# result_type = "error"  
# result_message = "This is a success message."  

# custom_messagebox("Message", result_message, result_type)
