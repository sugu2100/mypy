import turtle as t
import random

t.shape("turtle")

t.speed(0)
t.up()
x = random.randint(-250, 250)
y = random.randint(-250, 250)
t.goto(x, y)

t.mainloop()
