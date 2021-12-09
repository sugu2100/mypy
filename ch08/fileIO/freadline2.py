
f = open('c:/pyfile/season.txt', 'r')
#reason = f.readline()  # 한줄(첫줄) 읽기
#print(season)
seasons = f.readlines()  # 전체 라인 읽기
print(seasons)  # 리스트로 반환
print(seasons[0])
print(seasons[-1])

for season in seasons:
   #print(season)
   print(season.strip())  #한줄 공백 제거

f.close()


