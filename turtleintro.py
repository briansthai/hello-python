import turtle
t = turtle.Pen()
turtle.bgcolor("black")
turtle.speed(10)
sides = 6
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for x in range(360):
    t.pencolor(colors[x%len(colors)])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)