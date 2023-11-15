import turtle


t = turtle.Turtle()
t.speed(0)
turtle.title('Lill')

t.fillcolor('blue')
for i in range(0, 12):
    t.begin_fill()
    t.right(30)
    t.circle(30)
    t.forward(30)
    t.end_fill()
    

t.begin_fill()
t.right(180)
t.fd(15)
t.right(90)
t.fd(10)
t.left(90)
t.circle(70)
t.fillcolor('yellow')
t.end_fill()
t.hideturtle()

turtle.mainloop()