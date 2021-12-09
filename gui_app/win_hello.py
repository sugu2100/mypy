from tkinter import *

root = Tk()
root.title("hello")
root.geometry("200x60")

frame = Frame(root)
frame.pack()

Label(frame, text="Hello~ python!!", font=("Times", 16)).grid(row=0, column=0)
Button(frame, text='확인').grid(row=1, column=0)

root.mainloop()
