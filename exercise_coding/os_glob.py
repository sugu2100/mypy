
import os
import glob

# pyfile 찾기
os.chdir('c:/')
dir = os.popen('dir')
print(dir.read())

# 모든 txt파일 읽기
file = glob.glob('c:/pyfile/*.txt')
print(file)

# 특정 파일의 내용 읽기
with open('c:/pyfile/kbo2021.txt', 'r') as f:
    data = f.read()
    print(data)

