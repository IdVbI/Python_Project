import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')

value = [str(i)+'일' for i in range(1,32)]
combobox = ttk.Combobox(root, height = 5, values = value, state = 'readonly') # 읽기 전용으로 사용자가 임의변경 불가능
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목 설정

def btn1_cmd():
    print(combobox.get()) # 선택된 값 출력

btn1 = Button(root, text = '선택', command = btn1_cmd)
btn1.pack()

root.mainloop()