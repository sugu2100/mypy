from class_lib.student import Student

# 객체 리스트 생성
s = [
    Student("김하나", 1),
    Student("이두울", 2),
    Student("박세엣", 3),
]

#print(s[0])
print("******* 학생 명단 *******")
for i in s:
    print(i)

