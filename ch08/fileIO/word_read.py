# 이차원 리스트로 만들기
with open('animal.txt', 'r') as f:
    """
    for i in range(4):
        data = f.readline().split()
        print(data)
    """
    li = []
    for i in range(4):
        li.append(f.readline().split())
    print(li)

    for i in range(4):
        print(li[i][0])


