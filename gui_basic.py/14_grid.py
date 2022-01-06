from tkinter import *

root = Tk()
root.title('SB Ten Key') # 제목
root.geometry('280x480+400+200')
root.resizable= False
'''
button1 = Button(root, text='1')
button2 = Button(root, text='2')

button1.grid(row = 0, column = 0)
button2.grid(row = 1, column = 1)
'''

# 1번 줄
btn_F16 = Button(root, text = 'F16', width = 2, height = 2).grid(row = 0, column = 0)
btn_F17 = Button(root, text = 'F17', width = 2, height = 2).grid(row = 0, column = 1)
btn_F18 = Button(root, text = 'F18', width = 2, height = 2).grid(row = 0, column = 2)
btn_F19 = Button(root, text = 'F19', width = 2, height = 2).grid(row = 0, column = 3)

# 2번 줄
btn_clear = Button(root, text = 'clear', width = 2, height = 2).grid(row = 1, column = 0)
btn_equal = Button(root, text = '=', width = 2, height = 2).grid(row = 1, column = 1)
btn_div = Button(root, text = '/', width = 2, height = 2).grid(row = 1, column = 2)
btn_mul = Button(root, text = '*', width = 2, height = 2).grid(row = 1, column = 3)

# 3번 줄
btn_7 = Button(root, text = '7', width = 2, height = 2).grid(row = 2, column = 0)
btn_8 = Button(root, text = '8', width = 2, height = 2).grid(row = 2, column = 1)
btn_9 = Button(root, text = '9', width = 2, height = 2).grid(row = 2, column = 2)
btn_sub = Button(root, text = '-', width = 2, height = 2).grid(row = 2, column = 3)

# 4번 줄
btn_4 = Button(root, text = '4', width = 2, height = 2).grid(row = 3, column = 0)
btn_5 = Button(root, text = '5', width = 2, height = 2).grid(row = 3, column = 1)
btn_6 = Button(root, text = '6', width = 2, height = 2).grid(row = 3, column = 2)
btn_plu = Button(root, text = '+', width = 2, height = 2).grid(row = 3, column = 3)

# 5번 줄
btn_1 = Button(root, text = '1', width = 2, height = 2).grid(row = 4, column = 0)
btn_2 = Button(root, text = '2', width = 2, height = 2).grid(row = 4, column = 1)
btn_3 = Button(root, text = '3', width = 2, height = 2).grid(row = 4, column = 2)
btn_ent = Button(root, text = 'enter', width = 2, height = 5).grid(row = 4, column = 3, rowspan = 2)

# 6번 줄
btn_0 = Button(root, text = '0', width = 8, height = 2).grid(row = 5, column = 0, columnspan = 2)
btn_point = Button(root, text = '.', width = 2, height = 2).grid(row = 5, column = 2)




root.mainloop()