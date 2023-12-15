from tkinter import *
import ctypes

WIDTH, HEIGHT = map(lambda x: ctypes.windll.user32.GetSystemMetrics(x), (0, 1))
ELEM_WIDTH = 10
FONT = ('Georgia 20')

root = Tk()
root.title('Primitive calculator')
root.geometry(f'{WIDTH // 5}x{HEIGHT // 3}+{WIDTH // 3}+{HEIGHT // 3}')

class CustomButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['width'] = ELEM_WIDTH
        self['font'] = FONT
        self['width'] = ELEM_WIDTH
        self['bg'] = 'white'
        self['fg'] = 'blue'


class Block(Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        Frame.__init__(self, master, background='white')
        self.ent1 = Entry(master, width=ELEM_WIDTH, font=FONT, fg='blue')
        self.ent2 = Entry(master, width=ELEM_WIDTH, font=FONT, fg='blue')
        self.but_add = CustomButton(master, text='+')
        self.but_sub = CustomButton(master, text='-')
        self.but_mul = CustomButton(master, text='*')
        self.but_div = CustomButton(master, text='/')
        self.result = Label(master, width=ELEM_WIDTH, bg='black', fg='yellow', font=FONT)

        self.but_add['command'] = self.add
        self.but_sub['command'] = self.sub
        self.but_mul['command'] = self.mul
        self.but_div['command'] = self.div

        self.ent1.pack()
        self.ent2.pack()
        self.but_add.pack()
        self.but_sub.pack()
        self.but_mul.pack()
        self.but_div.pack()
        self.result.pack()

    def add(self) -> None:
        self.but_add['activebackground'] = '#181920'
        self.but_add['activeforeground'] = '#012345'
        num1 = float(self.ent1.get())
        num2 = float(self.ent2.get())
        calculation = num1 + num2
        self.result['text'] = self.__demonstrate(calculation)

    def sub(self) -> None:
        num1 = float(self.ent1.get())
        num2 = float(self.ent2.get())
        calculation = num1 - num2
        self.result['text'] = self.__demonstrate(calculation)

    def mul(self) -> None:
        num1 = float(self.ent1.get())
        num2 = float(self.ent2.get())
        calculation = num1 * num2
        self.result['text'] = self.__demonstrate(calculation)

    def div(self) -> None:
        num1 = float(self.ent1.get())
        num2 = float(self.ent2.get())
        if num2 == 0:
            self.result['text'] = 'Division by 0!'
        else:
            calculation = num1 / num2
            self.result['text'] = self.__demonstrate(calculation)

    def __demonstrate(self, value):
        if value % 1 == 0 and value < 1e9:
            return int(value)
        if abs(value) > 1e6 or abs(value) < 1e-6:
            return f'{value:.3e}'
        return f'{value:.3f}'


block = Block(root)
root.mainloop()