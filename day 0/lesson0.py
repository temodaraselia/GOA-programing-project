from turtle import *

#we want to paint a house

#step 1: draw a square

speed(15)


width(7)
color("blue")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
left(90)
color("yellow")
begin_fill()
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
left(150)
left(60)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(30,200)
pendown()
#drawing window


left(28)
forward(60)
left(94)
forward(60)
left(87)
forward(60)
left(180)
forward(30)
right(90)
forward(60)

left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
right(90)
forward(110)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(180)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)


exitonclick()