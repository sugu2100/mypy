from tkinter import *
from converters import Converters

class App:
    def __init__(self, master):
        self.con = Converters('C', 'F', 1.8, 32)  # 객체 생성
        frame = Frame(master)
        frame.pack()

        Label(frame, text='deg C').grid(row=0, column=0)
        self.c = DoubleVar()  # 실수 값을 구하는 클래스
        Entry(frame, textvariable = self.c).grid(row=0, column=1)

        Label(frame, text='deg F').grid(row=1, column=0)
        self.f = DoubleVar()
        Label(frame, textvariable = self.f).grid(row=1, column=1)
        Button(frame, text="변환", command = self.convert).grid(row=2, columnspan=2)

    def convert(self):
        c = self.c.get() # get() 가져오기
        # 변환해서 소수 2자리까지 출력
        conv_f = "{: .2f}".format(self.con.convert(c))
        self.f.set(conv_f)   # set() 지정하기

root = Tk()
root.title("Temperature Converter")
root.geometry("250x100+200+200")
app = App(root)   #App 클래스의 app 객체 생성

root.mainloop()
