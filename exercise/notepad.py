# 작은 메모장 만들기
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    with open('memo.txt', 'a') as f:
        f.write(memo)
        f.write('\n')
elif option == '-v':
    with open('memo.txt', 'r') as f:
        memo = f.read()
        print(memo)

#print(option)
#print(memo)