import re

p = re.compile("(?P<name>\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-5678")
print(m.group("name"))
