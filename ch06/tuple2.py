import random

answers = (
    "자! 해보세요!",
    "됐네요, 이 사람아",
    "뭐라고? 다시 생각해보세요",
    "모르니 두려운 것입니다.",
    "칠푼인가요?? 제 정신이 아니군요!",
    "당신이라면 할 수 있어요!",
    "해도 그만, 안 해도 그만, 아니겠어요?",
    "맞아요, 당신은 올바른 선택을 했어요"
    )

print("안녕하세요~ Magic 상담소입니다.");

question = input("조언을 구하고 싶으면 질문을 입력하고\n엔터 키를 누르세요.\n")

print("고민 중...\n" * 4)

choice = random.randint(0, 7)
print(answers[choice])
