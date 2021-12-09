import os
import glob

os.chdir("c:/")
dir = os.popen('dir')
print(dir.read())

file = glob.glob('c:/pyfile/*.txt')
print(file)

with open('c:/pyfile/kbo2021.txt', 'r') as f:
    data = f.read()
    print(data)