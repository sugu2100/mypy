import re

str = "123?45yy7890 hi 999 hello"
# compile()후 findall() - 검색할 내용이 많은 경우(속도 빠름)
pat = re.compile("\d{1,3}") # 1~3개 검색
m = re.findall(pat, str)
print(m)

# findall()로 검색한 경우
m2 = re.findall('[A-z]', str)
print(m2)

m3 = re.findall("[1-5]{1,2}", str)
print(m3)
