from tkinter import *
import os
from PIL import Image
import pyttsx3

# ----------------------- SOUND -------------------------------------#
engine = pyttsx3.init() 
engine.setProperty('rate', 200) 
engine.setProperty('volume', 1.0)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def say(phrase):
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ONE_SECOND = 1000
PATH = os.path.dirname(__file__)
TITLES = ('Пора работать', 'Перерыв 20 минут', 'Перерыв 5 минут', 'Помодоро')
MAXLENGTH = len(max(TITLES, key=len))
reps = 0
timer = None
is_pause = False

class CustomButton(Button):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self['highlightthickness'] = 0
        self['border']  =0
        self['bg'] = GREEN
        self['font'] = (FONT_NAME, 24, "bold")
        self['fg'] = RED
        self['text'] = kwargs['text']
        self['command'] = kwargs['command']



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, is_pause
    root.after_cancel(timer)
    reps = 0
    is_pause = False
    label.config(text=f'{TITLES[-1]: ^{MAXLENGTH}}', fg=GREEN)
    checkmark_label.config(text='')
    canvas.itemconfig(timer_text, text='00:00')

# ------------------------------ PAUSE -----------------------------------#
def set_pause():
    global is_pause, timer
    is_pause = not is_pause
    if is_pause:
        pause_button.config(text='Continue')
        say('Ставлю паузу')
    else:
        say('Продолжаем')
        pause_button.config(text='Pause')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        label.config(text=f'{TITLES[0]: ^{MAXLENGTH}}', fg=RED)
        say(TITLES[0])
        countdown(WORK_MIN * 60)
    elif reps % 8 == 0:
        label.config(text=f'{TITLES[1]: ^{MAXLENGTH}}', fg=GREEN)
        say(TITLES[1])
        countdown(LONG_BREAK_MIN * 60)
        reps = 0
    else:
        label.config(text=f'{TITLES[2]: ^{MAXLENGTH}}', fg=GREEN)
        say(TITLES[2])
        countdown(SHORT_BREAK_MIN * 60)
    if reps % 2 == 0:
        checkmark_label.config(text=f'{CHECKMARK * (reps // 2)}')
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer, is_pause
    canvas.itemconfig(timer_text, text=f'{count // 60:0>2}:{count % 60:0>2}')
    if count >= 0:
        if not is_pause:
            timer = root.after(ONE_SECOND, countdown, count - 1)
        else:
            timer = root.after(ONE_SECOND, countdown, count)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.geometry('800x480+800+300')
root.config(padx=15, pady=10, bg=YELLOW)

img_name = os.path.join(PATH, 'tomato.png')

with Image.open(img_name) as image:
    image.load()
    img_width, img_height = image.size

canvas = Canvas(root, width=img_width, height=img_height, bg=YELLOW, highlightthickness=0)
photo_img = PhotoImage(file=img_name)
canvas.create_image(img_width // 2 + 1, img_height // 2 + 3, image=photo_img)
timer_text = canvas.create_text(img_width // 2 + 1, img_height // 2 + 13, text='00:00', fill=YELLOW, font=(FONT_NAME, 36, 'bold'))

label = Label(root, text=f'{TITLES[-1]: ^{MAXLENGTH}}', font=(FONT_NAME, 36, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
start_button = CustomButton(root, text='Start', command=start_timer)
reset_button = CustomButton(root, text='Reset', command=reset_timer)
pause_button = CustomButton(root, text='Pause', command=set_pause)
checkmark_label = Label(root, text='', highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 36, "bold"), foreground=GREEN)

label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_label.grid(row=3, column=1)
pause_button.grid(row=4, column=1)
root.mainloop()