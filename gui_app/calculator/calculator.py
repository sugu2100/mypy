from tkinter import *

def click1():
    display.insert(END, '1')

def click2():
    pass

root = Tk()
root.title("나의 계산기")

display = Text(root, width=20, height=1)
display.grid(row=0, column=0)
Button(root, text='1', width=5, command=click1).grid(row=1, column=0)

root.mainloop()