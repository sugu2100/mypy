from tkinter import *

def click():
    text = entry.get()
    output.delete(0.0, END)
    output.insert(END, text)

 # 텍스트 박스 내용 지움(0.0-줄번호.시작 문자)
 #  END - 문자열이 입력된 최종지점까지 삭제후 삽입

root = Tk()
root.title("hello")

Label(root, text="이름 : ").grid(row=0, column=0)
entry = Entry(root, width=10)
entry.grid(row=0, column=1)
Button(root, text='확인', command=click).grid(row=1, columnspan=2)
Label(root, text="출력 : ").grid(row=2, column=0)
# s = StringVar()
# output = Label(root, textvariable=s)
# output.grid(row=2, column=1)
output = Text(root, width=20, height=5)
output.grid(row=2, columnspan=2)


root.mainloop()
