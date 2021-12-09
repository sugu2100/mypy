
f = open("C:/pyfile/number.txt", 'w')

f.write("%d\n" % 300)
f.write("%.1f\n" % 7.3)
num = "%d\n" % 100000
f.write(num)

f.close()