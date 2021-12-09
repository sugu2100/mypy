'''
# 사용자가 입력한 데이터의 길이 출력
user_msg = input('메시지 입력: ')
len = len(user_msg)
print('메시지 길이: {}'.format(len))
'''

# 개인정보 포맷문자열로 출력
# 주민등록증(identification card)
name = input('이름 입력: ')
user_id = input('아이디 입력: ')
pw = input('비밀번호 입력 : ')
id_card1 = input('주민번호 앞자리 입력: ')
id_card2 = input('주민번호 뒷자리 입력: ')

print('='*30)
print("이름 {}".format(name))
print("아이디 {}".format(user_id))
pw_hidden = '*' * len(pw)
print("비밀번호 {}".format(pw_hidden))
id_card_hidden = id_card2[0] + ('*' * 6)
print('주민번호 : {0}-{1}'.format(id_card1, id_card_hidden))
print('='*30)
