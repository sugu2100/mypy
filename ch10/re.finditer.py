import re

str = "123?45yy7890 hi 999 Hello"

m1 = re.findall("\d{1,3}", str)
print(m1)

m2 = re.finditer("[A-Za-z]+", str)
#print(m2)
for i in m2:
    print(i)


