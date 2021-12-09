import os
import glob

os.chdir('c:/pydb')  # pydb 디렉터리로 이동

dir = os.popen('dir')   # dir 명령을 실행

print(dir.read())       # dir 결과 출력


data = glob.glob('c:/pyworks/exercise/*.py')
print(data)