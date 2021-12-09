from tkinter import *
from converters import Converters

class App:
    def __init__(self, master):
        self.conv = Converters('C', 'F', 1.8, 32)
        frame = Frame(master)
        frame.pack()

        Label(frame, text='deg C').grid(row=0, column=0)
        self.c = DoubleVar()
        Entry(frame, textvariable = self.c).grid(row=0, column=1)

        Label(frame, text='deg F').grid(row=1, column =0)
        self.f = DoubleVar()
        Label(frame, textvariable=self.f).grid(row=1, column=1)

        Button(frame, text='변환', command=self.convert).grid(row=2, columnspan=2)

    def convert(self):
        c = self.c.get()   #섭씨 온도 가져와서
        f = self.conv.convert(c)  #화씨 온도로 변환
        self.f.set(f)   #화씨 온도에 대입

root = Tk()
root.title("Temperature Converter")

app = App(root)  #root를 전달해서 app 객체 생성

root.mainloop()
