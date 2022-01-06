from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')

def create_new():
    print('새 파일을 만듭니다.')

def create_window():
    print('새 윈도우를 만듭니다.')

menu = Menu(root)

# File
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = 'New file', command = create_new)
menu_file.add_command(label = 'New window', command = create_window)
menu_file.add_separator()
menu_file.add_command(label = 'Open file...')
menu_file.add_separator()
menu_file.add_command(label = 'Save all', state = 'disable') # 비활성화
menu_file.add_separator()
menu_file.add_command(label = 'Exit', command = root.quit)

menu.add_cascade(label = 'File', menu = menu_file)

# Edit
menu_edit = Menu(menu, tearoff = 0)

menu.add_cascade(label = 'Edit', menu = menu_edit)

# Radio

menu_lang = Menu(menu, tearoff = 0)
menu_lang.add_radiobutton(label = 'C++')
menu_lang.add_radiobutton(label = 'Java')
menu_lang.add_radiobutton(label = 'Python')

menu.add_cascade(label = 'Language', menu = menu_lang)

# View

menu_view = Menu(menu, tearoff = 0)
menu_view.add_checkbutton(label = 'Show Minimap')
menu.add_cascade(label = 'View', menu = menu_view)

root.config(menu = menu)
root.mainloop()