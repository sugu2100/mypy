from tkinter import *

def click():
    name = ent_name.get()
    email = ent_email.get()
    print(name, email)

root = Tk()
root.title("회원 가입")
root.geometry("230x130+200+200")

Label(root, text="").grid(row=0, column=0, sticky=W)
Label(root, text="  이름  ").grid(row=1, column=0, sticky=W)
ent_name = Entry(root, width=20)
ent_name.grid(row=1, column=1, sticky=W)

Label(root, text="  이메일  ").grid(row=2, column=0, sticky=W)
ent_email = Entry(root, width=20)
ent_email.grid(row=2, column=1, sticky=W)
Label(root, text="").grid(row=3, column=0, sticky=W)
Button(root, text="가입", width=10, command=click).grid(row=4, columnspan=2)

root.mainloop()
