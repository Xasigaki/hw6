import turtle

tt=turtle.Turtle()
turtle.bgcolor("yellow")
tt.pencolor("red")

tt.speed(0)
tt.penup()
tt.goto(0,200)
tt.pendown()

fd=0
dR=0

while(True):
    tt.forward(fd)
    tt.right(dR)
    fd+=3
    dR+=1
    if dR==210:
        break
    tt.hideturtle()

turtle.done()