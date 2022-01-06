from abc import update_abstractmethods
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')


'''
progressbar = ttk.Progressbar(root, maximum = 100, mode = 'determinate') # mode : determinate, indeterminate
progressbar.start(20)
progressbar.pack()


def btn1_cmd():
    progressbar.stop()

btn1 = Button(root, text = '중지', command = btn1_cmd)
btn1.pack()
'''

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btn2_cmd():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var2.set(i)
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn2= Button(root, text = '시작', command = btn2_cmd)
btn2.pack()

root.mainloop()