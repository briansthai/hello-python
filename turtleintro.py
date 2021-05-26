import turtle

sides = eval(turtle.textinput("Sides", "Enter the number of sides"))
print(sides)

screen = turtle.Screen()
t = turtle.Pen()
turtle.bgcolor("black")
turtle.speed(10)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for x in range(360):
    t.pencolor(colors[x%len(colors)])
    t.penup()
    t.forward(x * 3/sides + x)
    t.pendown()
    t.write("its me brian!", font = ("Arial", int((x+4)/4), "bold"))
    t.left(360/sides + 1)
