
with open('animal.txt', 'r') as f:
    line = f.readline()  # 1줄 읽기
    print(line)

    lines = f.readlines() # 전체 읽기
    print(lines)  # 1차원 리스트로 반환
    # for i in lines:
    #     print(i)

    # 2차원 리스트로 기억
    animal = []
    for i in lines:
        #animal.append([i])
        animal.append([i[0:3]]) #'\n'을 제외
    print(animal)

