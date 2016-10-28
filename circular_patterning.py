import turtle

brush = turtle.Turtle()
brush.speed(100)
brush.pensize(5)

for i in range(36):
    if i % 2 == 0:
        brush.color("black")
    else:
        brush.color("gray")
    brush.right(10)
    for j in range(36):
        brush.right(10)
        brush.forward(20)

input("Press enter to close")
