#Create separate functions for drawing a square and triangle

import turtle

def draw_triangle():
    for i in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.forward(75)

def draw_square():
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.forward(75)


turtle.goto(-250,0)
draw_triangle()
draw_square()

input("Press enter to close window.")




















#
# def draw_square():
#     for i in range(0,4):
#         turtle.forward(50)
#         turtle.left(90)
#     turtle.forward(100)
#
# def draw_triangle():
#     for i in range(0,3):
#         turtle.forward(50)
#         turtle.left(120)
#     turtle.forward(100)
#
# turtle.penup()
# turtle.goto(-200,0)
# turtle.pendown()
#
# draw_square()
# draw_triangle()
#
# input("Press enter to continue.")
