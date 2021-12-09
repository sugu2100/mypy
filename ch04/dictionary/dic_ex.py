
dic = {'kor':90, 'eng':70, 'math':80}
print(dic.keys())

print(list(dic.keys()))  # 키를 리스트로 변환

print(dic.values())
print(list(dic.values())) # 값을 리스트로 변환


print(tuple(dic.values())) # 값을 튜플로 변환

print(set(dic.values())) # 값을 set으로 변환

"""
# 키값만 가져옴 
print(list(dic))
print(tuple(dic))
print(set(dic))
"""

