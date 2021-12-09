import re

# 이름과 전화번호 분리 - ()소괄호 사용
p = re.compile("(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-5678")
# print(m.group(1))
# print(m.group(2))

# (?<그룹 이름>)
p2 = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
m2 = p2.search("park 010-1234-5678")
# print(m2.group("name"))
# print(m2.group("phone"))

a = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
s = a.sub("\g<1>-****", "kim 010-1234-5678")
print(s)