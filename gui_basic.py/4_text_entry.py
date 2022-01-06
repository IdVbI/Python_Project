from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')

txt = Text(root, width = 50, height = 30)
txt.pack()

txt.insert(END, '글자를 입력해 주세요.')

e = Entry(root, width = 30) # 한 줄로 입력을 받을 때
e.pack()
e.insert(0,'비밀번호를 입력해 주세요.')

def btn_cmd():
    # 내용 출력
    print(txt.get('1.0',END)) # 1 = cjtqjsWo fkdls, 0 = 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)

btn = Button(root, text = '확인', command = btn_cmd)
btn.pack()

root.mainloop()