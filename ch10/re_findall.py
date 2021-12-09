import re

# re.compile()을 사용하지 않고 정규 표현식 사용
str = "Two is too"
m1 = re.findall("T[ow]o", str)
print(m1)

# re.IGNORECASE - 대, 소문자 구분 않음
m2 = re.findall("T[ow]o", str, re.IGNORECASE)
print(m2)

m3 = re.findall("t[^w]o", str, re.IGNORECASE)
print(m3)