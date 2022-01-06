from tkinter import *

root = Tk()
root.title('SB GUI') # 제목

root.geometry('640x480+400+200')

bt1 = Button(root, text = '버튼')
bt1.pack()

bt2 = Button(root, padx = 5, pady = 10, text = '취소 취소 취소')
bt2.pack()

bt3 = Button(root, padx = 10, pady = 20, text = '실행') # 버튼 글자 + 여백의 크기
bt3.pack()

bt4 = Button(root, width = 1, height = 2, text = '입력') # 고정된 크기
bt4.pack()

bt5 = Button(root, fg = 'blue', bg = 'yellow', text = '색상') # 버튼 색상
bt5.pack()

pht = PhotoImage(file = '/Users/limseongbin/Downloads/Pyhton Project/pygame_basic/PISXEL/Golem.gif') # 이미지 버튼
bt6 = Button(root, image = pht)
bt6.pack()

def bt7_cmd():
    print('동작하였음')

bt7 = Button(root, text = '동작', command = bt7_cmd) # 버튼 coomand
bt7.pack()

root.mainloop()