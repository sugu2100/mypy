
with open('animal.txt', 'r') as f:
    #lines = f.readlines() #전체 읽기
    #print(lines) - 리스트로 반환
    # for line in lines:
    #     print(line)

    # 2차원 리스트에 저장
    animal = []
    for i in range(4):
        animal.append(f.readline().split())
    print(animal)

    # 리스트 목록 출력
    for i in animal:
        print(i)

