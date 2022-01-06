from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')

Label(root, text = '메뉴를 선택하세요.').pack()


set_var = IntVar()
btn_burger1 = Radiobutton(root, text = '불고기 버기 세트', value = 1, variable = set_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text = '치즈 버기 세트', value = 2, variable = set_var)
btn_burger3 = Radiobutton(root, text = '새우 버기 세트', value = 3, variable = set_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = '음료를 선택하세요.').pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = '콜라', value = '콜라', variable= drink_var)
btn_drink2 = Radiobutton(root, text = 'ZERO 콜라', value = 'ZERO 콜라', variable= drink_var)
btn_drink1.pack()
btn_drink1.select()

btn_drink2.pack()


def btn1_cmd():
    # 선택된 값 출력
    print(set_var.get())

def btn2_cmd():
    # 선택된 값 출력
    print(drink_var.get())

btn1 = Button(root, text = '메뉴주문', command = btn1_cmd)
btn1.pack()

btn2 = Button(root, text = '음료주문', command = btn2_cmd)
btn2.pack()

root.mainloop()