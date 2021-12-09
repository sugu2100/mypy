import re

p = re.compile("[a-z]+")
m = p.match("2020 python")  # 처음부터 일치해야 찾음
print(m)

s = p.search("2020 python") # 전체를 찾아서 일치하면 됨
print(s)


print(s.group())  # group()은 문자열로 출력

