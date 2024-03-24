
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import subprocess
import pyaudio
import wave
import tkinter as tk
import threading
from pathlib import Path
import time
import sys

import pygame
from scores import addScore3, center_window
from findScore import clear, clear1, clear2, clear3
sys.path.append('AudioDyslexia')

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, IntVar, Radiobutton
from AudioDyslexia.resutl import AudioRecord

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\YusrGP\YusrProject\assets\frame9")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
window.title('Letters')

window.geometry("396x688")
window.configure(bg = "#FFEDED")


#---------- Calculate Score --------------
# ---------- track the selected value of a radio button ----------
radio_var1 = IntVar()



#------------------------ voice recording ------------------------
timerValue = tk.IntVar()
def timerfunction():
    for i in range(3, 0, -1):
        counter['text'] = str(i)
        counter.update_idletasks()
        time.sleep(1)
    counter['text'] = "0"

def record_audio(filename, duration, sample_rate, channels):
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=1024
    )

    print("Recording...")

    frames = []
    for _ in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))


def record_and_save_audio(filename, duration=1, sample_rate=44100, channels=1):
    #--------------- Create a thread for the timer ------------------
    counter_thread = threading.Thread(target=timerfunction)
    counter_thread.start()

    #-------------- Create a thread for audio recording ----------------
    audio_thread = threading.Thread(target=record_audio, args=(filename, duration, sample_rate, channels))

    audio_thread.start()

#-----------------------------------------------
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
    201.0,
    630.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    200.0,
    320.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    199.0,
    137.0,
    image=image_image_3
)

pygame.init()
def perform_action(event):
    sound = pygame.mixer.Sound(r"C:\YusrGP\YusrProject\assets\frame9\Letter.mp3")
    sound.play()
canvas.tag_bind(image_3, "<Button-1>", perform_action)

#------------button Recording the letter qaf -------------
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Radiobutton(image=button_image_1,
borderwidth=0,
indicatoron=0,
variable=radio_var1,
value=2,
highlightthickness=0,
command=lambda: record_and_save_audio("recorded_audio1.wav"))

button_1.place(
    x=174.0,
    y=395.0, 
    width=51.0,
    height=52.0
)

#------------timing of audio recording---------
counter = tk.Label(bg="#FFEDED", text ="3", font = ("Arial", 12))
counter.place(x=207, y=455)

counter0 = tk.Label(bg="#FFEDED", text =":0", font = ("Arial", 12))
counter0.place(x=193, y=455)

counter00 = tk.Label(bg="#FFEDED", text ="00", font = ("Arial", 12))
counter00.place(x=175, y=455)


# ----------------- function nextpage and alert ------------------
def open_QafHarakatPage():
    if radio_var1.get() != 0 or radio_var1.get() != 0:
        score = 0 
        if radio_var1.get() == 1: #  زر لم يتعرف 
            score += 2
        elif radio_var1.get() == 2:
            AudioRecord(r"C:\YusrGP\YusrProject\recorded_audio1.wav",id1="gaf",id2="ga")
        addScore3(score)
        file_to_run_path = r"C:\YusrGP\YusrProject\QafHarakatPage.py"
        window.destroy()
        subprocess.run(["python", file_to_run_path], check=True)
       #window.destroy()  # Destroy the current window and open page two
       #import QafHarakatPage.py
    else:
        messagebox.showwarning(title="تنبيه", message="اكمل حل السؤال")

# ----------------- button nextpage ------------------
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
image=button_image_2,
borderwidth=0,
highlightthickness=0,
command=open_QafHarakatPage, # Call the function to open page two
relief="flat"

)
button_2.place(
    x=143.0,
    y=584.0,
    width=117.0,
    height=57.0
)

#------button لم يتعرف
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Radiobutton(
    image=button_image_3,
    indicatoron=0,
    borderwidth=0,
    highlightthickness=0,
    variable=radio_var1, 
    value=1,
    relief="flat"
)

button_3.place(
    x=91.0,
    y=490.0,
    width=220.0,
    height=63.0
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
