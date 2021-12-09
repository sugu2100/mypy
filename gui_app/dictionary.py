from tkinter import *

def click():
    try:
        word = entry.get()
        output.delete(0.0, END)
        definition = dic[word]
        output.insert(END, definition)
    except:
        output.insert(END, "단어의 정의를 찾을 수 없습니다.")

window = Tk()
window.title("용어 사전")
Label(window, text="단어를 입력하고 엔터 키를 누르세요").grid(row=0, column=0, sticky=W)
entry = Entry(window, width=20, bg="lightgreen")
entry.grid(row=1, column=0, sticky=W)
Button(window, text="제출", width=10, command=click).grid(row=2, column=0, sticky=W)
Label(window, text="정의").grid(row=3, column=0, sticky=W)
output = Text(window, width=80, height=10, bg="lightgreen")
output.grid(row=4, column=0, sticky=W)

dic = {"알고리즘": "컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해 놓은 것",
       "버그": "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각",
       "이진수": "2진법으로 나타낸 숫자, 0과 1로 구성됨",
       "html": "하이퍼 텍스트 마크업 언어로 웹 페이지를 구성하는 언어이다.",
       "CSS": "웹 페이지를 구성하는 요소로 디자인을 담당하는 웹 기술이다.",
       "대화형 모드": "IDLE(Python IDE-통합개발환경)을 벗어나 코드를 저장하지 않고 테스트할 때 사용",
       "함수": "재사용 가능한 코드 조각"
}


window.mainloop()
