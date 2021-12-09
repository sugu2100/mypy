# 파일을 읽어서 2차원 리스트로 만들기
with open('animal.txt', 'r') as f:
    #line1 = f.readline()
    #print(line1)  #dog

    li =[]
    for i in range(4):
        line = f.readline().split()
        print(line)
        li.append(line)
    print(li)

    # 전체 요소 출력
    for i in range(4):
        print(li[i][0])

