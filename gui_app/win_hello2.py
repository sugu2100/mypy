from tkinter import *

def click():
    print("안녕~ 파이썬")  # 콘솔창에 출력

root = Tk()
root.title("hello")
root.geometry("200x70")

frame = Frame(root)
frame.pack()

Label(frame, text="Hello~").grid(row=0, column=0)
Button(frame, text='확인', command=click).grid(row=1, column=0)

root.mainloop()


