from tkinter import *

def click():
    try:
        word = entry.get()
        text.delete(0.0, END) #0.0 - 줄번호.문자 위치
        definition = dic[word]
    except KeyError:
        definition = "단어의 정의를 찾을 수 없습니다."
    text.insert(END, definition)  # END-최종 입력 지점

root = Tk()
root.title("용어 사전")

Label(root, text="정의되어 있는 단어를 입력하고 엔터 키를 누르세요").grid(row=0, column=0, sticky=W)
entry = Entry(root, width=20, bg="sky blue")
entry.grid(row=1, column=0, sticky=W)
Button(root, text="제출", width=10, command=click).grid(row=2, column=0, sticky=W)
# click은 괄호를 포함하면 버튼을 눌렀을때가 아닌 생성한 시점에서 함수가 실행된다.
Label(root, text="정의 : ").grid(row=3, column=0, sticky=W)
text = Text(root, width=80, height=10, bg="sky blue")
text.grid(row=4, column=0, sticky=W)

dic = {
    "알고리즘": "컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해 놓은 것",
    "버그": "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각",
    "이진수": "2진법으로 나타낸 숫자, 0과 1로 구성됨",
    "html": "하이퍼 텍스트 마크업 언어로 웹 페이지를 구성하는 언어이다.",
    "CSS": "웹 페이지를 구성하는 요소로 디자인을 담당하는 웹 기술이다.",
    "함수": "재사용 가능한 코드 조각"
}
root.mainloop()


