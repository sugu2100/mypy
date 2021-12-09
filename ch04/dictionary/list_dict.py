# 학생 5명의 국어, 수학 성적 계산
# 리스트 선언 - 요소는 딕셔너리로 선언
students =[
    {'name': '이대한', 'korean': 88, 'math':77, 'python': 95},
    {'name': '장민국', 'korean': 82, 'math':65, 'python': 85},
    {'name': '오상식', 'korean': 58, 'math':83, 'python': 75},
    {'name': '천선란', 'korean': 99, 'math':91, 'python': 85},
    {'name': '김초엽', 'korean': 94, 'math':87, 'python': 75},
]

# 개인별 총점과 평균
print(' 이름  총점 평균')
for student in students:    # 학생을 1명씩 반복
    total = student['korean'] + student['math'] + student['python'] #국어, 수학 점수를 가져옴
    avg = total / 3
    print("%s %d %.1f" % (student['name'], total, avg))   # 출력

# 과목별 총점과 평균
sum_kor = 0
sum_math = 0
sum_py = 0
for student in students:
    sum_kor += student['korean']
    sum_math += student['math']
    sum_py += student['python']

avg_kor = sum_kor / 5
avg_math = sum_math / 5
avg_py = sum_py / 5
print("국어 합계 : %d점" % sum_kor)
print("수학 합계 : %d점" % sum_math)
print("python 합계 : %d점" % sum_py)
print("국어 평균 : %.1f점" % avg_kor)
print("수학 평균 : %.1f점" % avg_math)
print("python 평균 : %.1f점" % avg_py)
