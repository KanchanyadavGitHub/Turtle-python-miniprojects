import turtle
s=turtle.getscreen()
t1=turtle.Turtle()
t1.pensize(5)
t1.pencolor("purple")
t1.circle(60)
t1.begin_fill()
t1.fillcolor("red")
t1.goto(-100,-100)
t1.goto(100,-100)
t1.goto(0,0)
t1.end_fill()
t1.penup()
t1.fillcolor("red")
t1.goto(-30,-100)
t1.pendown()
t1.goto(-30,-190)
t1.penup()
t1.goto(30,-100)
t1.pendown()
t1.goto(30,-190)
t1.penup()
t1.pencolor("black")
t1.goto(200,-190)
t1.pendown()
t1.goto(-600,-190)


s.mainloop()