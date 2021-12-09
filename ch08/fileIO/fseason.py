# 계절을 파일로 저장하기
season = ['봄', '여름', '가을', '겨울']
f = open("c:/pyfile/season.txt", 'w')
for i in season:
    f.write(i + '\n')

# for i in range(len(season)):
#     f.write(season[i] + '\n')
f.close()

f = open("c:/pyfile/season.txt", 'r')
data = f.read()
print(data)
f.close()

