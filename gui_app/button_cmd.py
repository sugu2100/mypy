from tkinter import *

def click():
    en_text = entry.get()
    text.delete(0.0, END) #0행 0열
    text.insert(END, en_text)

root = Tk()
root.title("hello")
root.geometry("200x100+200+200")

frame = Frame(root)
frame.pack()

Label(frame, text="이름 : ").grid(row=0, column=0)
entry = Entry(frame, width=15)
entry.grid(row=0, column=1)
Button(frame, text='확인', width=10, command=click).grid(row=1, columnspan=2)
text = Text(frame, width=25, height=3)
text.grid(row=2, columnspan=2)

root.mainloop()
