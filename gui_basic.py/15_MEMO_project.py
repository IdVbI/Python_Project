import os
from tkinter import *

root = Tk()
root.title('SB MEMO') # 제목
root.geometry('640x480+400+200')

# menu
menu = Menu(root)

# menu 함수

filename = 'mynote.txt'

def open_cmd():
    if os.path.isfile(filename):
        with open(filename, 'r', encoding = 'utf8') as file:
            txt.delete('1.0', END)
            txt.insert(END, file.read())

def save_cmd():
    with open(filename, 'w', encoding = 'utf8') as file:
        file.write(txt.get('1.0', END))

# File
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label = 'Open', command=open_cmd)
menu_file.add_command(label = 'Save', command=save_cmd)
menu_file.add_separator()
menu_file.add_command(label = 'Close', command=root.quit)

menu.add_cascade(label = 'File', menu = menu_file)

# Edit
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label = 'Edit', menu = menu_edit)

# State
menu_state = Menu(menu, tearoff=0)
menu.add_cascade(label = 'State', menu = menu_edit)

# View
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label = 'View', menu = menu_view)

# Help
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label = 'Help', menu = menu_help)

# scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# memo 본문
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side='left',fill='both', expand=True)
scrollbar.config(command=txt.yview)

root.config(menu = menu)
root.mainloop()