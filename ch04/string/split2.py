n = input("세 개의 수 입력 : ")
a = n.split()  # 입력한 값을 리스트 a 에 저장
print(a)

sum = 0
for i in a:
    sum += int(i)  # a는 문자열이므로 정수로 바꿈

print(sum)
