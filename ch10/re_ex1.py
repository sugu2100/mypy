import re

# '*'와 '+'의 차이
p = re.compile("ca*t")  #앞 문자가 0번 이상 반복(즉 없어도 찾음)
m1 = re.findall(p, "caat")
print(m1)
m2 = re.findall(p, "ct")
print(m2)

p2 = re.compile("ca+t")  # 앞 문자가 1번 이상 반복(즉, 없으면 못찾음)
m3 = re.findall(p2, "caat")
print(m3)
m4 = re.findall(p2, "ct")  # 없음 [] 빈 리스트
print(m4)
