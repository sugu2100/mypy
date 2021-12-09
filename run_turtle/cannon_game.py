# 거북이 대포 게임
import turtle as t
import random

def turn_up():
    t.left(2)    #거북이를 왼쪽으로 2도 돌림

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()   # 현재 거북이가 바라보는 각도 저장

    while t.ycor() > 0:  # 거북이가 땅위에 있는 동안 반복
        t.forward(15)
        t.right(5)

    # 거북이가 while을 빠져나가면 땅에 닿은 상태임(y좌표 : 0)
    d = t.distance(target, 0)        # 거북이와 목표 지점과의 거리
    t.sety(random.randint(10, 100))  # 문자열을 출력할 y좌표 위치
    if d < 25:  # 거리 차이가 25보다 작으면 명중한 것으로 처리
        t.color('blue')
        t.write("Good!", False, "center", ("", 15))
    else:
        t.color('red')
        t.write("Bad!", False, "center", ("", 15))
        t.color('black')
        t.goto(-200, 10)   # 거북이의 처음 위치 호출
        t.setheading(ang)  # 처음 저장한 각도를 호출

# 땅을 그린다
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점 설정
target = random.randint(50, 150)
t.pensize(3)
t.color('green')
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

# 거북이 위치 설정
t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)

# 키보드 작동
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()

t.mainloop()
