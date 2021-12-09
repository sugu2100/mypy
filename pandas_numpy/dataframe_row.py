import pandas
# 데이터프레임 행 다루기

dict = {'c0':[1,2,3], 'c1':[4,5,6]}
df = pandas.DataFrame(dict, index=['r0', 'r1', 'r2'])
print(df, '\n')

# 행 선택
row0 = df.iloc[0]   #iloc - 인덱스 번호를 인수로 가짐
row1 = df.iloc[1]
row2 = df.loc['r2'] #loc - 행 인덱스의 이름을 사용

print(row0, '\n')
print(row1, '\n')
print(row2, '\n')

# 행 추가
df.loc['r3'] = 10, 20
print(df, '\n')

df.loc['r4'] = 0
print(df, '\n')

# 행 변경
df.loc['r3'] = df.loc['r4']
print(df, '\n')

# 행 삭제
df.drop('r4', axis=0, inplace=True)
print(df, '\n')

df.drop(['r1', 'r3'], axis=0, inplace=True)
print(df)