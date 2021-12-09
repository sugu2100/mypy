import os

os.chdir("c:/pyworks")

result = os.popen("dir")
print(result.read())