import sys

src = sys.argv[1]
src2 = sys.argv[2]

f = open(src, 'r')
tab = f.read()
f.close()

space = tab.replace('\t', " "*4)
print(space)

f = open(src2, 'w')
f.write(space)
f.close()
#print(src)
#print(src2)


