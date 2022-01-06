from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')


chkvar = IntVar() # 체크바에 인트형으로 값을 저장
checkbox = Checkbutton(root, text = '오늘 하루 보지 않기', variable = chkvar)
checkbox.select() # 자동 선택
checkbox.pack()

chkvar2 = IntVar() # 체크바에 인트형으로 값을 저장
checkbox2 = Checkbutton(root, text = '다시는 보지 않기', variable = chkvar2)
checkbox2.deselect() # 자동 선택 하지 않음
checkbox2.pack()


def btn1_cmd():
    # 0 = 체크 해제, 1 = 체크
    print(chkvar.get())
    print(chkvar2.get())


btn1 = Button(root, text = '확인', command = btn1_cmd)
btn1.pack()

root.mainloop()