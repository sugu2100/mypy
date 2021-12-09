from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        Label(frame, text='deg C').grid(row=0, column=0)
        Button(frame, text='변환', command=self.convert).grid(row=1, columnspan=2)

    def convert(self):
        print("Not implemented")

root = Tk()
root.title("Temp Converter")

app = App(root)  #root를 생성자 변수로 전달


root.mainloop()