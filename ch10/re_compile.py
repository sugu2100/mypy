import re

#compile -> byte 코드로 바꿈
p1 = re.compile("[a-z]+")

str = "happiness"
m1 = p1.match(str)
print(m1)
print(m1.group())

m2 = re.findall("[a-z]+", "Hello")
print(m2)


"""
p1 = re.compile("\w+")
result = p1.match("afternoon")
print(result)
print(result.group())
"""