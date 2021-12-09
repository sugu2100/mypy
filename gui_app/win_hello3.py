from tkinter import *

def click():
    text = entry.get()   # 입력한 텍스트 가져옴
    print(text + "님 환영합니다.")

root = Tk()
root.title("hello")
root.geometry("200x70")

frame = Frame(root)
frame.pack()

Label(frame, text="이름 : ").grid(row=0, column=0)
entry = Entry(frame, width=10)
entry.grid(row=0, column=1)
Button(frame, text='확인', command=click).grid(row=1, columnspan=2)

root.mainloop()
