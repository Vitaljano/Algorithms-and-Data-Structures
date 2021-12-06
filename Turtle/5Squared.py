import turtle

"""Draw 10 square"""
cnt = 10
a = 10
s = 10
turtle.shape('turtle')
turtle.goto(0, 0)
for i in range(1, cnt + 1, 1):
    print(i)
    turtle.pendown()
    for j in range(0, 4):
        turtle.forward(a)
        turtle.left(90)
    else:
        turtle.penup()
        turtle.goto(-s*i, -s*i)
    a += s*2
