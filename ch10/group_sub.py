import re

p = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
s = p.sub("\g<name> \g<phone>", "park 010-1111-2222")
print(s)
