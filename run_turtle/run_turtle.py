import turtle as t
import random

def turn_right():
    t.setheading(0)
    
def turn_up():
    t.setheading(90)
    
def turn_left():
    t.setheading(180)
    
def turn_down():
    t.setheading(270)
    
def play():
    # 적 거북이가 주인공 거북이쪽 보며 쫒아가기
    t.forward(10)
    te.forward(9)
    ang = te.towards(t.pos())
    te.setheading(ang)

    # 게임 시작(실행시간-0.1초)
    # 적거북이가 주인공거북이에게 닿으면 게임 종료
    if t.distance(te) >= 12:
        t.ontimer(play, 100)

    # 주인공 거북이가 먹이에 닿으면 다시 새 위치에서 무작위로 나타남
    if t.distance(tf) < 12:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)

# 적 거북이
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200)

# 주인공 거북이 , 전체 스테이지(무대)
t.tilt("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()

t.mainloop()
