import turtle as t

t.shape('turtle')
'''
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
'''
for i in range(4):
    t.forward(100)  # 거리 100px
    t.right(90)  # 각도 90도

for i in range(3):
    t.forward(100)
    t.left(120)

t.circle(50)   # 반지름이 50


