import random

say1 = "자! 해보세요!"
say2 = "됐네요, 이 사람아"
say3 = "뭐라고? 다시 생각해보세요"
say4 = "모르니 두려운 것입니다."
say5 = "칠푼인가요?? 제 정신이 아니군요!"
say6 = "당신이라면 할 수 있어요!"
say7 = "해도 그만, 안 해도 그만, 아니겠어요?"
say8 = "맞아요, 당신은 올바른 선택을 했어요"

print("안녕하세요~ Magic 상담소입니다.");
question = input(
"""조언을 구하고 싶으면 질문을 입력하고
엔터 키를 누르세요""")
print("고민 중...\n" * 4)

choice = random.randint(1, 8)
if choice == 1:
    answer = say1
elif choice == 2:
    answer = say2
elif choice == 3:
    answer = say3
elif choice == 4:
    answer = say4
elif choice == 5:
    answer = say5
elif choice == 6:
    answer = say6
elif choice == 7:
    answer = say7
else:
    answer = say8

print(answer)
input("마치려면 엔터 키를 누르세요")













    
