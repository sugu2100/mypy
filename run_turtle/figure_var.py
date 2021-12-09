import turtle as t

t.shape('turtle')

n = 4
for i in range(n):
    t.forward(100)  
    t.right(360/n)  

n = 3
t.color("red")
t.pensize(3)
for i in range(n):
    t.forward(100)
    t.left(360/n)

t.color("blue")
t.pensize(2)
t.circle(50)   


