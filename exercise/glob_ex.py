import glob
import os

os.chdir("c:/")
find = os.popen('dir')
print(find.read())

data = glob.glob("c:/pyfile/*.txt")
print(data)

f = open("c:/pyfile/2021kbo.txt", 'r')
word = f.read()
print(word)



