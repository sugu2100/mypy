#dict

dic = {"알고리즘": "컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해 놓은 것",
       "버그": "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각",
       "이진수": "2진법으로 나타낸 숫자, 0과 1로 구성됨",
       "html": "하이퍼 텍스트 마크업 언어로 웹 페이지를 구성하는 언어이다.",
       "CSS": "웹 페이지를 구성하는 요소로 디자인을 담당하는 웹 기술이다.",
       "함수": "재사용 가능한 코드 조각"
}

print("♣ 용어 사전 ♣")
x = input("정의되어 있는 단어를 입력하세요 : ")
try:
    definition = dic[x]
    print(definition)
except KeyError :
    print("찾는 단어가 없습니다.")
