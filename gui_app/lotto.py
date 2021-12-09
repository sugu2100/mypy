from tkinter import *

def lotto():
    import requests
    from bs4 import BeautifulSoup

    num = entry.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={0}".format(num)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs = {'class', 'win_result'}).get_text()
    num_list = txt.split('\n')[7:13]
    bonus = txt.split('\n')[-4]

    print('당첨 번호')
    print(num_list)
    print('보너스 번호')
    print(bonus)

window = Tk()
window.geometry("300x100")
window.title("로또 당첨")
#win.option_add("*Font", "고딕 16")
entry = Entry(window)
entry.grid(row=0, column=0, sticky=W)
#entry.pack()
btn = Button(window, text = '로또 당첨 번호 확인', command=lotto)
btn.grid(row=1, column=0, sticky=W)
#btn.config(text = '로또 당첨 번호 확인')
window.mainloop()
