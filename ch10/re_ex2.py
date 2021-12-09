import re

# 점(.)은 임의의 문자 , 괄호()는 서브클래스
# - 태그를 제외하고 괄호 안의 내용 매칭
str = "abcd<hr>Thank you"
pat1 = re.compile("<(.*)>")
m1 = re.findall(pat1, str)
print(m1)

# 태그 포함하여 괄호 안의 내용 매칭
pat2 = re.compile("(<.*>)")
m2 = re.findall(pat2, str)
print(m2)
