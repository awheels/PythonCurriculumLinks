#Create a single function for drawing a polygon of any number of sides

import turtle

turtle.speed(2)

def draw_shape(sides, colour):

    turtle.color(colour)

    for i in range(0, sides):
        turtle.forward(20)
        turtle.left(360/sides)
    turtle.forward(100)

turtle.penup()
turtle.goto(-300,0)
turtle.pendown()

draw_shape(3, "green")
draw_shape(5, "blue")
draw_shape(6, "purple")
draw_shape(7, "black")
draw_shape(12, "red")

input("Press enter to continue.")
