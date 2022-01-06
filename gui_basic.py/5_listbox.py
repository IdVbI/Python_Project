from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')

# 리스트
# if selectmode = single : 하나만 선택 가능 // height = 3 : 3개만 표시 키보드로 내려서 확인 가능
listbox = Listbox(root, selectmode = 'extended', height = 0)
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()


def btn1_cmd():

    print('리스트에는', listbox.size(), '개가 있습니다.')

def btn2_cmd():
    # 내용 삭제
    listbox.delete(END)

def btn3_cmd():
    # 내용 확인 
    print('1부터 3번째까지의 항목 :', listbox.get(0,2))

def btn4_cmd():
    # 내용 확인 
    print('선택된 항목', listbox.curselection())


btn1 = Button(root, text = '개수', command = btn1_cmd)
btn1.pack()

btn2 = Button(root, text = '삭제', command = btn2_cmd)
btn2.pack()

btn3 = Button(root, text = '확인', command = btn3_cmd)
btn3.pack()

btn4 = Button(root, text = '선택', command = btn4_cmd)
btn4.pack()


root.mainloop()