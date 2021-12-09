# 파일 쓰기 - 숫자형
f = open('number.txt', 'w')
#f.write(300)
f.write("%d \n" % 300)
f.write("%.1f \n" % 7.3)
num = "%d" % 1000000
f.write(num)

f.close()

