import turtle
t = turtle.Pen()
turtle.bgcolor("black")
turtle.speed(10)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for x in range(10,100):
    t.pencolor(colors[x%len(colors)])
    t.circle(x)
    t.left(360/len(colors))