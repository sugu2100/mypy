import os

# 디렉터리 검색
os.chdir("c:/pyworks")
dir = os.popen('dir')
print(dir.read())


# 디렉터리 이름 검색
dirnames = os.listdir("c:/pyworks")
for dirname in dirnames:
    print(dirname)

# 파일 이름 검색
filenames = os.listdir("c:/pyworks/exercise")
print(filenames)
for filename in filenames:
    print(filename)

