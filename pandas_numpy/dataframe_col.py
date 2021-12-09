import pandas
# 데이터프레임 열 다루기

dict = {'c0':[1,2,3], 'c1':[4,5,6]}
df = pandas.DataFrame(dict, index=['r0', 'r1', 'r2'])
print(df, '\n')

#열 선택
col0 = df['c0']
col1 = df.c1

print(col0)
print(col1)

# 열 추가
df['c2'] = 7, 8, 9
print(df, '\n')

df['c3'] = 0
print(df, '\n')

df['c4'] = df['c3']
print(df, '\n')

# 열 변경
df['c3'] = 10, 11, 12
print(df, '\n')

df['c3'] = 0

#열 삭제
df.drop('c4', axis=1, inplace=True)
print(df, '\n')
# axis=1 옵션 - 열, axis=0 옵션 - 행
# inplace=True 기존 데이터에 변경 내용 반영

df.drop(['c1', 'c3'], axis=1, inplace=True)
print(df)