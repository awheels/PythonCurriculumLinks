#Create a single function for drawing a square and triangle and add colour

import turtle

def draw_shape(shape, colour):

    turtle.color(colour)

    if shape == 'square':
        for i in range(0,4):
            turtle.forward(50)
            turtle.left(90)
        turtle.forward(75)

    elif shape == 'triangle':
        for i in range(0,3):
            turtle.forward(50)
            turtle.left(120)
        turtle.forward(75)


turtle.penup()
turtle.goto(-200,0)
turtle.pendown()

draw_shape('triangle', 'red')
draw_shape('square', 'black')


input("Press enter to continue.")
