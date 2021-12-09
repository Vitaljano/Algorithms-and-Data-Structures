import turtle

turtle.shape('turtle')
cnt = 20
lng = 100
t = 360 / cnt;
for i in range(0, cnt):
    turtle.forward(lng)
    turtle.stamp()
    turtle.back(lng)
    turtle.left(t)