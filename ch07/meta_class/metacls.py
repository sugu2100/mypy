# type()함수를 이용하여 동적으로 클래스 생성하기
Hello = type("Hello", (), {}) # 문자열, 튜플, 딕셔너리
print(Hello)

hello = Hello()
print(hello)
