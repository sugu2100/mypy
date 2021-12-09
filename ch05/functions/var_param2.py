# 가변 매개변수 - 변수앞에 '*' 붙임
def calc_avg(*numbers):
    sum_v = 0
    avg = 0.0
    for i in numbers:
        sum_v += i
    avg = sum_v / len(numbers)
    return avg

avg1 = calc_avg(1, 2)
avg2 = calc_avg(1, 2, 3, 4)
print(avg1)
print(avg2)


