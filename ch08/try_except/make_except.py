# 사용자 정의 예외 클래스는 Exception 클래스를 상속 받아 만든다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보' or nick == '칠푼이':
        raise MyError()
    print(nick)

try:
    say_nick('영웅')
    say_nick('바보')
    say_nick('칠푼이')
except MyError as e:
    print(e)
