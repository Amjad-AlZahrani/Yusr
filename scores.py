def addScore1(score):
    with open("score1.txt", "a") as file:
        file.write(str(score) + "\n")

def addScore2(score):
    with open("score2.txt", "a") as file:
        file.write(str(score) + "\n")

def addScore3(score):
    with open("score3.txt", "a") as file:
        file.write(str(score) + "\n")

def center_window(window):
    window.update_idletasks()  
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    window.geometry(f"+{x}+{y}")