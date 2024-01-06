from tkinter import *
from tkinter.messagebox import askyesno, showerror, showinfo
from calculator import calculate

# ------ COLORS ------------- #
COMMON_BACKGROUND = '#DCF2F1'
LABEL_BACKGROUND = '#A1EEBD'
BUTTON_BACKGROUND = '#FAEED1'
BUTTON_FOREGROUND = '#11235A'

FONT = ('COURIER', 24, 'bold')
# CONSTANTS
text = ''
# CLASSES
class CButton(Button):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self['bg'] = BUTTON_BACKGROUND
        self['fg'] = BUTTON_FOREGROUND
        self['font'] = FONT
        self['width'] = kwargs.get('width', 5) 
        self['height'] = 1
        self['borderwidth'] = 5
        self['activebackground'] = inverse_color(BUTTON_BACKGROUND)
        self['activeforeground'] = inverse_color(BUTTON_FOREGROUND)
        self.text = kwargs['text']

    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs)
        self['padx'] = 0
        self['pady'] = 0
        
class CLabel(Label):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self['bg'] = LABEL_BACKGROUND
        self['width'] = 17
        self['height'] = 2
        self['font'] = FONT

# FUNCTIONS
def inverse_color(color: str) -> str:
    r, g, b = map(lambda x: hex(255 - int(x, base=16))[2:].upper(), (color[1:3], color[3:5], color[5:]))
    return f'#{r:02}{g:02}{b:02}'

def insert_value(value: str) -> None:
    global text
    text += f'{value}'
    label_field.config(text=text)

def clear_screen() -> None:
    yes_no = askyesno('Clear field', 'Do yo want to clear entry field?')
    if yes_no:
        global text
        text = ''
        label_field.config(text=text)

def show_result():
    try:
        result = calculate(text)
    except Exception as e:
        showerror('Error', e)
    else:
        result = int(result) if int(result) == result else result
        showinfo('result', result)

# MAIN PART

root = Tk()
root.geometry('325x545+500+200')
root.title('Calculator')
root.config(bg=COMMON_BACKGROUND)
root.resizable(width=0, height=0)

# ----------------- ELEMENTS ----------------- #
label_field = CLabel(root)

buttons_numbers = [CButton(root, text=f'{i % 10}',
                           command=lambda i=i: insert_value(str(i % 10))) for i in range(1, 11)]
buttons_brackets = [CButton(root, text=symbol,
                            command=lambda symbol=symbol: insert_value(symbol)) for symbol in '()']

# buttons_ops = [CButton(root, text=symbol,
#                       command=lambda symbol=symbol: insert_value(symbol)) for symbol in SIMPLE_OPERATIONS]

button_add = CButton(root, text='+', command=lambda: insert_value('+'))
button_sub = CButton(root, text='-', command=lambda: insert_value('-'))
button_mul = CButton(root, text='*', command=lambda: insert_value('*'))
button_div = CButton(root, text='/', command=lambda: insert_value('/'))
button_eq = CButton(root, text='=', command=show_result)
button_clear = CButton(root, text='C', command=clear_screen)
button_dot = CButton(root, text='.', command=lambda: insert_value('.'))
button_pow = CButton(root, text='^', command=lambda: insert_value('^'))
button_mod = CButton(root, text='%', command=lambda: insert_value('%'))

# ------------- ELEMENT DEMONSTRATION -------- #
label_field.grid(row=0, column=0, columnspan=3)

for idx, nb in enumerate(buttons_numbers[:-1]):
    nb.grid(row=idx // 3 + 1, column=idx % 3)

buttons_numbers[-1].grid(row=4, column=1)

for idx, btn in enumerate(buttons_brackets):
    btn.grid(row=4, column=idx * 2)


button_add.grid(row=5, column=0)
button_sub.grid(row=5, column=1)
button_eq.grid(row=5, column=2)
button_mul.grid(row=6, column=0)
button_div.grid(row=6, column=1)
button_pow.grid(row=6, column=2)
button_dot.grid(row=7, column=0)
button_mod.grid(row=7, column=1)
button_clear.grid(row=7, column=2)

root.mainloop()