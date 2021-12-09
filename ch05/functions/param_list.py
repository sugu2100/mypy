# 리스트가 매개변수인 함수 정의
def calc_age(a):
    sum_v = 0
    for i in a:
        sum_v += i
    avg = sum_v / len(a)
    return avg

v = [70, 90, 50, 80, 100]
average = calc_age(v)

print("평균 :", average)
