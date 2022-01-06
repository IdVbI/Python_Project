from tkinter import *

root = Tk()
root.title('SB GUI') # 제목

root.geometry('640x480+400+200')

label1 = Label(root, text = '안녕하세요')
label1.pack()

pht = PhotoImage(file='/Users/limseongbin/Downloads/Pyhton Project/pygame_basic/PISXEL/Mini_Devil.gif')
label2 = Label(root, image = pht)
label2.pack()

def bt_cmd():
    label1.config(text = '반가워요')

    global pht2 # 글로벌로 바꿔야 불필요한 메모리 공간 해체를 피할 수 있음
    pht2 = PhotoImage(file='/Users/limseongbin/Downloads/Pyhton Project/pygame_basic/PISXEL/RED_SLIME.gif') 
    label2.config(image=pht2)


bt = Button(root, text = '입력', command = bt_cmd)
bt.pack()

root.mainloop()