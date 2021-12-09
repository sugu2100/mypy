# 파일 쓰기
f = open('c:/pyfile/number.txt', 'w')
#f.write(14)
f.write("%d\n" % 14)
f.write("%.1f\n" % 7.3)
sum_v = "%d" % eval("100+200")  # eval(문자열식) -> 숫자 계산
f.write(sum_v)
f.close()

