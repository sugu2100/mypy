import turtle as t


def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)


def polygon2(n, d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)


polygon(3)
polygon(5)

t.up()   # 선 올리기
t.forward(100)  
t.down() # 선 내리기

polygon2(3, 75)
polygon2(5, 100)
