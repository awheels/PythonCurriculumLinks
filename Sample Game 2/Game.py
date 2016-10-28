import turtle
import random
import math
import time

gameOver = False
score = 0
# Game Window Creation
window = turtle.Screen()
window.title("Catch Dem Tentacles")
window.addshape("Character1.gif")
window.bgpic("back.gif")
window.addshape("yum.gif")
window.setup(600,600)
window.tracer(3)

#Create Border
border = turtle.Turtle()
border.hideturtle()
border.speed(1000)
border.penup()
border.goto(-250,250)
border.pendown()
border.pensize(5)

for x in range(4):
    border.forward(500)
    border.right(90)

#Title of game
border.penup()
border.goto(0,265)
border.write("Get to 50.", align="center", font=("Cambria",20, "normal"))

#Create Player
player = turtle.Turtle()
player.penup()
player.goto(0, -100)
player.shape("Character1.gif")



#Game Controls
def up():
    if(player.ycor() < 235):
        player.goto(player.xcor(), player.ycor()+5)


def down():
    if (player.ycor() > -235) :
        player.goto(player.xcor(), player.ycor()-5)


def left():
    if(player.xcor() > -235):
         player.goto(player.xcor()-5, player.ycor())


def right():
    if(player.xcor() < 235):
         player.goto(player.xcor()+5, player.ycor())

maxGoals = 10
goalsList = []

for count in range(maxGoals):
    goalsList.append(turtle.Turtle())
    goalsList[count].shape("yum.gif")
    goalsList[count].penup()
    goalsList[count].right(90)
    goalsList[count].speed(random.randint(2,8))
    goalsList[count].goto(random.randint(-200, 200),210)

turtle.listen()
turtle.onkey(down, "Down")
turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 40:
        return True
    else:
        return False

while not gameOver:

    for count in range(maxGoals):
        goalsList[count].forward(goalsList[count].speed())

        if goalsList[count].ycor() < -200:
              goalsList[count].setposition(random.randint(-200,200),210)

        if isCollision(player,goalsList[count]):
            goalsList[count].setposition(random.randint(-200,200),210)
            border.undo()
            score += 1
            border.penup()
            border.setposition(-220, 220)
            border.write("Score:"+str(score), False, align="left", font=("Arial", 14, "normal"))

            if score == 5:
                border.goto(-200, 0)
                border.write("GAME OVER! YOU HAVE ENOUGH TENTACLES FOR A FEAST", False, align="left", font=("Arial", 15, "normal"))
                gameOver = True

