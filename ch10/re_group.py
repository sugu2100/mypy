import re

p = re.compile('[a-z]+')
m = p.match("hello")

print(m.group())
print(m.start())
print(m.end())