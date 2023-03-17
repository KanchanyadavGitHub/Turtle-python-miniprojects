import turtle
s= turtle.getscreen()
turtle.ht()
s.title("mooving turtle like fan")
t1=turtle.Turtle()
t1.pencolor("yellow")
t1.shape("turtle")

t1.shapesize(10,10,10)
for i in range(0,901,90):
    t1.left(90)
s.mainloop()
    