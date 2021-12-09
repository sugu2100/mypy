# 딕셔너리
# 딕셔너리 생성과 관리
person = {}  #빈 딕셔너리
print(person)
print(type(person))

# 요소 추가
person["name"] = "한국민"
person["age"] = 28
person["phone"] = "010-1234-5678"
print(person)

# 1개 요소 출력
print(person["name"])

# 전체 출력
for key in person:
    print(key)          #key 출력
    print(person[key])  #value 출력
print('*' * 50)

# 딕셔너리 함수
print(person.keys())
print(person.values())
print(person.items())
print(list(person.items()))

for key, value in person.items():
    print(key, value)

# key로 value 얻기
print(person.get("age"))

# 요소 삭제
print(person.pop('phone'))
print(person)

