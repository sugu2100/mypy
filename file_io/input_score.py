
with open('score.txt', 'a') as f:
    name = input("이름 입력 : ")
    kor = int(input("국어 점수 : "))
    math = int(input("수학 점수 : "))
    avg = (kor + math) / 2

    f.write(name + ' ')
    f.write(str(kor) + ' ')
    f.write(str(math) + ' ')
    f.write(str(avg) + '\n')

