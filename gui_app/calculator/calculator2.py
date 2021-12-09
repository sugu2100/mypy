from tkinter import *

def click(key):
    if key == '=':
        try:
            value = eval(display.get())  # 계산값(숫자)
            result = str(value)[0:10]  # 문자로 출력(10개)
            display.insert(END, '=' + result)
        except:
            display.insert(END, "-->오류")
    elif key == 'C':
        display.delete(0, END)  # 첫번째 문자 위치부터 삭제
    else:
        display.insert(END, key)

root = Tk()
root.title("나의 계산기")

# top_row 프레임
top_row = Frame(root)
top_row.grid(row=0, column=0, columnspan=2, sticky=N) #위에 배치
display = Entry(top_row, width=50, bg='light green')
display.grid(row=0, column=0)

# 숫자 버튼 프레임
num_pad = Frame(root)
num_pad.grid(row=1, column=0, sticky=W)  #왼쪽에 배치
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]
r = 0
c = 0
for btn_txt in num_pad_list:
    def cmd(x=btn_txt): # 함수에 인수를 전달하는 방법
        click(x)

    Button(num_pad, text=btn_txt, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:  #2열을 초과하면
        c = 0
        r = r + 1

# 연산자 프레임 생성
operator = Frame(root)
operator.grid(row=1, column=1, sticky=E) #오른쪽에 배치
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']

r =0
c = 0
for btn_txt in operator_list:
    def cmd(x=btn_txt):
        click(x)

    Button(operator, text=btn_txt, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 1:  #1열을 초과하면
        c = 0
        r = r + 1

root.mainloop()