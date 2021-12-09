
import sys

# 명령 행에서 인수를 전달함
args = sys.argv[1:]
print(args)

total = 0
for i in args:
    total += int(i)

print(total)

"""
# 전체 요소 출력
for i in args:
    print(i)
"""