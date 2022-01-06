import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('SB GUI') # 제목
root.geometry('640x480+400+200')

# 알림
def info():
    msgbox.showinfo('알림', '정상예매 되었습니다.')

def warn():
    msgbox.showwarning('경고', '모든 좌석이 매진 되었습니다.')

def err():
    msgbox.showerror('오류', '결제 오류가 발생했습니다.')

def cancel():
    msgbox.askokcancel('예매', '해당 좌석은 노약자석입니다. 예매하시겠습니까?')

def retrycancel():
    msgbox.askretrycancel('재시도', '일시적 오류가 발생했습니다. 예매하시겠습니까?')

def yesno():
    response1 = msgbox.askyesno('예 / 아니요', '해당 좌석은 역방향 입니다. 예매하시겠습니까?')

    if response1 == 1:
        print('예')
    elif response1 == 0:
        print('아니오')


def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message='예매 내역이 저장되지 않았습니다.\n저장하시지 않고 종료하시겠습니까?')
    # 네 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : ㅍ츠로그램 종료 취소  
    print('응답 :',response) # True,Fasle,None == 1, 0, 그 외
    if response == 1:
        print('예')
    elif response == 0:
        print('아니오')
    else:
        print('취소')

Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=err, text='오류').pack()

Button(root, command=cancel, text='예매').pack()
Button(root, command=retrycancel, text='재예매').pack()
Button(root, command=yesno, text='예 아니요').pack()
Button(root, command=yesnocancel, text='예 아니요 취소').pack()



root.mainloop()