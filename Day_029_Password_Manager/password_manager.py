from string import ascii_letters, digits, punctuation
from tkinter import Tk, Entry, Button, Label, Canvas, PhotoImage
from tkinter import messagebox
import sqlite3 as sql
import hashlib
import random
import pyperclip
import os


# ------------- COLORS AND CONSTANTS ----------- #
GREEN = '#52D3D8'
YELLOW = '#F4F27E'
RED = '#750E21'
DARKBLUE = '#31304D'
PURPLE = '#7B66FF'
LIME = '#EEF296'
FONTSIZE = 18
ENTRY_FONT = ('ComicSans', FONTSIZE)
BUTTON_FONT = ('Courier', FONTSIZE, 'bold')
PATH = os.path.dirname(__file__)

# ----------------- CLASSES -------------------- #
class CustomEntry(Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['bg'] = YELLOW
        self['fg'] = RED
        self['font'] = ENTRY_FONT
        self['highlightthickness'] = 0
        self['justify'] = 'center'
        self.bind("<Control-BackSpace>", self.delete_whole_line)
        self.bind("<Control-Delete>", self.delete_whole_line)
    
    def delete_whole_line(self, event):
        self.delete(0, 'end')

class CustomButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['bg'] = DARKBLUE
        self['fg'] = YELLOW
        self['activebackground'] = PURPLE
        self['activeforeground'] = LIME
        self['font'] = BUTTON_FONT
        self['highlightthickness'] = 0
        self['text'] = kwargs['text']
    
    def grid(self, **kwargs):
        kwargs.setdefault('padx', 5)
        kwargs.setdefault('pady', 5)
        super().grid(**kwargs)

class CustomLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['bg'] = GREEN
        self['fg'] = RED
        self['font'] = BUTTON_FONT
        self['highlightthickness'] = 0
        self['text'] = kwargs['text']

    def grid(self, **kwargs):
        kwargs.setdefault('padx', 5)
        kwargs.setdefault('pady', 5)
        super().grid(**kwargs)

# -------------- FUNCTIONS --------------------- #
def generate_password():
    number = random.randint(8, 16)
    alphabet = ascii_letters + digits + punctuation
    password = ''.join(random.choices(alphabet, k=number))
    entry_password.delete(0, 'end')
    entry_password.insert(0, password)

def copy_password():
    password = entry_password.get()
    pyperclip.copy(password)

def hash_string(input_string, algorithm='sha256'):
    hasher = hashlib.new(algorithm)
    hasher.update(input_string.encode('utf-8'))
    return hasher.hexdigest()

def insert_data():
    site = entry_site.get().strip().lower()
    email = entry_email.get().strip().lower()
    password = entry_password.get()
    if not site:
        messagebox.showerror("Error", "You did not fill the site field.")
        return
    if not email:
        messagebox.showerror("Error", "You did not fill email field.")
        return
    if not password:
        messagebox.showerror('Error', "Which password do you wanna safe?")
        return
    site = hash_string(site)
    email = hash_string(email)
    update = False
    try:
        curr_password = cursor.execute("SELECT password from sites WHERE site = ? AND email = ?", (site, email)).fetchall()
        if len(curr_password) > 0:
            cursor.execute("UPDATE sites SET password = ? WHERE site = ? AND email =?", (password, site, email))
            update = True
        else:
            cursor.execute("INSERT INTO sites (site, email, password) VALUES (?, ?, ?)", (site, email, password))
        con.commit()
        messagebox.showinfo('Info', f'Data is {("recorded", "updated")[update]}.')
    except Exception as e:
        print(f'Something went wrong: {e}')
        messagebox.showerror('Error', message=e)

def get_data():
    site = entry_site.get().strip().lower()
    email = entry_email.get().strip().lower()
    if not site:
        messagebox.showerror("Error", "You did not fill the site field.")
        return
    if not email:
        messagebox.showerror("Error", "You did not fill email field.")
        return
    site = hash_string(site)
    email = hash_string(email)
    try:
        request = cursor.execute("SELECT password from sites WHERE site = ? AND email = ?", (site, email)).fetchall()
        if len(request) == 0:
            messagebox.showerror("Error", "No such line in database")
            return
        else:
            entry_password.delete(0, 'end')
            entry_password.insert(0, request[0][0])
    except Exception as e:
        print(f'Something went wrong, {e}')
        messagebox.showerror('Error', message=e)

def delede_data():
    site = entry_site.get().strip().lower()
    email = entry_email.get().strip().lower()
    if not site:
        messagebox.showerror("Error", "You did not fill the site field.")
        return
    if not email:
        messagebox.showerror("Error", "You did not fill email field.")
        return
    site = hash_string(site)
    email = hash_string(email)
    try:
        cursor.execute("DELETE FROM sites WHERE site = ? AND email = ?", (site, email))
        con.commit()
        messagebox.showinfo('Info', message='Information is deleted.')
    except Exception as e:
        print(f'Something went wrong', e)
        messagebox.showerror('Error', message=e)

# ------------------ MAIN ---------------------- #
if __name__ == "__main__":
    con = sql.connect(os.path.join(PATH, 'data.db'))
    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sites (
        id INTEGER PRIMARY KEY,
        site TEXT,
        email TEXT,
        password TEXT
    )
    ''')

    root = Tk()
    root.title("Password Manager")
    root.geometry("800x500+200+200")
    root.config(bg=GREEN, padx=50, pady=50)

    canvas = Canvas(root, width=200, height=200)
    img = PhotoImage(file=os.path.join(PATH, 'logo.png'))
    canvas.create_image(100, 100, image=img)
    canvas.config(bg=GREEN, highlightthickness=0)

    label_site = CustomLabel(root, text='Site')
    entry_site = CustomEntry(root)
    button_delete = CustomButton(root, text='Delete', command=delede_data)

    label_email = CustomLabel(root, text='E-mail')
    entry_email = CustomEntry(root)

    label_password = CustomLabel(root, text='Password')
    entry_password = CustomEntry(root)
    button_password = CustomButton(root, text='Generate password', command=generate_password)

    button_show = CustomButton(root, text='Show password', command=get_data)
    button_record = CustomButton(root, text='Record data', command=insert_data)
    button_copy = CustomButton(root, text='Copy password', command=copy_password)

    canvas.grid(row=0, column=1)
    label_site.grid(row=1, column=0)
    entry_site.grid(row=1, column=1)
    button_delete.grid(row=1, column=2)

    label_email.grid(row=2, column=0)
    entry_email.grid(row=2, column=1)

    label_password.grid(row=3, column=0)
    entry_password.grid(row=3, column=1)
    button_password.grid(row=3, column=2)

    button_show.grid(row=4, column=0)
    button_record.grid(row=4, column=1)
    button_copy.grid(row=4, column=2)

    root.mainloop()
    con.close()
