# importing modules
import turtle
import time

startpuzzle = time.clock()


# Basic rules and instructions on how to play the game
def instructions():
    gmwindow.textinput("Thank you", "Thank you for Playing: THE CASE OF THE FISH. This is a puzzle game that is an interactive version of Einstein's Riddle.\nMy objective with this game is to create a game that requires the user to think in order to finish the game.\nNow, on to the storyline.")
    gmwindow.textinput("Story", "You are a very intelligent dog that has been hired by the police to find a thief.\nThis thief has stolen the world's rarest fish.\nThe police has traced the thief's position to a street with only five houses.\nAfter finding several clues along the street, you come to this conclusion:\n\nEach house has a different interior wall colour\nEach owner of each house has a different nationality\nEach house owner has their own specific drink\nEach house owner has their own specific type of food they like to eat\nEach house owner has a different pet, one of which is the fish.")
    gmwindow.textinput("Basic Information", "You can find your clues in the text file called CLUES.txt. Open that file and keep open at all times during the game.")
    gmwindow.textinput("Controls", "To control your player, use the WASD keys or the arrow keys. To enter the house you believe the thief is hiding in\n(You only have one chance, or else he will know you are trying to capture him and he will escape),\nwalk up to any of the house doors facing towards it.")
    gmwindow.textinput("Controls Continued", "If you need a hint, don't be ashamed of yourself,\nclick the button with the question mark on it.\nYou only have 3 hints, all of which are very helpful.")


# Setting up the game window and variables: Adding images, setting the screen size
gmwindow = turtle.Screen()
gmwindow.bgpic('StartScreen.gif')
gmwindow.setup(540, 540)
time.sleep(2)
gmwindow.bgpic('Background.gif')
gmwindow.addshape('sprite_dog1.gif')
gmwindow.addshape('sprite_dog2.gif')
gmwindow.addshape('sprite_dog3.gif')
gmwindow.addshape('sprite_dog4.gif')
gmwindow.addshape('sprite_dog5.gif')
gmwindow.addshape('sprite_dog6.gif')
gmwindow.addshape('sprite_dog7.gif')
gmwindow.addshape('sprite_dog8.gif')
gmwindow.addshape('house.gif')
gmwindow.addshape('InnerHouse1.gif')
gmwindow.addshape('InnerHouse2.gif')
gmwindow.addshape('InnerHouse3.gif')
gmwindow.addshape('InnerHouse4.gif')
gmwindow.addshape('InnerHouse5.gif')
gmwindow.addshape('Hint.gif')
gmwindow.addshape('Fish.gif')


hintnum = 0

"""Basic Controls: WASD keys and Up Down Left Right keys used to control the dog. Going left and right also moves the houses to give the game's
environment a more expansive feeling. Going forward also allows you to enter the houses in order to find the missing fish."""


def right():
    if player.xcor() <= 230:
        player.shape('sprite_dog1.gif')
        player.forward(2.5)
        player.shape('sprite_dog2.gif')
        time.sleep(0.1)
        player.forward(2.5)
        player.shape('sprite_dog1.gif')
    elif player.xcor() >= 230:
        player.shape('sprite_dog1.gif')
        player.shape('sprite_dog2.gif')
        time.sleep(0.1)
        player.shape('sprite_dog1.gif')
        house1.backward(5)
        house2.backward(5)
        house3.backward(5)
        house4.backward(5)
        house5.backward(5)


def left():
    if player.xcor() >= -240:
        player.shape('sprite_dog3.gif')
        player.backward(2.5)
        player.shape('sprite_dog4.gif')
        time.sleep(0.1)
        player.backward(2.5)
        player.shape('sprite_dog3.gif')
    elif player.xcor() <= -240:
        player.shape('sprite_dog3.gif')
        player.shape('sprite_dog4.gif')
        time.sleep(0.1)
        player.shape('sprite_dog3.gif')
        house1.forward(5)
        house2.forward(5)
        house3.forward(5)
        house4.forward(5)
        house5.forward(5)


def forward():
    if player.ycor() <= 0:
        player.shape('sprite_dog7.gif')
        player.sety(player.ycor() + 2.5)
        player.shape('sprite_dog8.gif')
        time.sleep(0.1)
        player.sety(player.ycor() + 2.5)
        player.shape('sprite_dog7.gif')
    if player.ycor() == 5:
        if player.xcor() == house1.xcor()+15:
            gmwindow.bgpic('InnerHouse3.gif')
            player.goto(180, -50)
            player.shape('sprite_dog3.gif')
            house1.goto(1000, 0)
            house2.goto(1000, 0)
            house3.goto(1000, 0)
            house4.goto(1000, 0)
            house5.goto(1000, 0)
            gmwindow.textinput("", "Oh no! The fish isn't here!\n The thief has now escaped, leaving you ashamed and bewildered...")
            exit()
        if player.xcor() == house2.xcor()+15:
            gmwindow.bgpic('InnerHouse4.gif')
            player.goto(180, -50)
            player.shape('sprite_dog3.gif')
            house1.goto(1000, 0)
            house2.goto(1000, 0)
            house3.goto(1000, 0)
            house4.goto(1000, 0)
            house5.goto(1000, 0)
            fish.showturtle()
            endpuzzle = time.clock()
            timeelapsed = (endpuzzle-startpuzzle)
            gmwindow.textinput("", "Congratulations! You found the fish!")
            gmwindow.textinput("", ("It took you", timeelapsed,"seconds."))
            exit()
        if player.xcor() == house3.xcor()+15:
            gmwindow.bgpic('InnerHouse2.gif')
            player.goto(180, -50)
            player.shape('sprite_dog3.gif')
            house1.goto(1000, 0)
            house2.goto(1000, 0)
            house3.goto(1000, 0)
            house4.goto(1000, 0)
            house5.goto(1000, 0)
            gmwindow.textinput("", "Oh no! The fish isn't here!\n The thief has now escaped, leaving you ashamed and bewildered...")
            exit()
        if player.xcor() == house4.xcor()+15:
            gmwindow.bgpic('InnerHouse5.gif')
            player.goto(180, -50)
            player.shape('sprite_dog3.gif')
            house1.goto(1000, 0)
            house2.goto(1000, 0)
            house3.goto(1000, 0)
            house4.goto(1000, 0)
            house5.goto(1000, 0)
            gmwindow.textinput("", "Oh no! The fish isn't here!\n The thief has now escaped, leaving you ashamed and bewildered...")
            exit()
        if player.xcor() == house5.xcor()+15:
            gmwindow.bgpic('InnerHouse1.gif')
            player.goto(180, -50)
            player.shape('sprite_dog3.gif')
            house1.goto(1000, 0)
            house2.goto(1000, 0)
            house3.goto(1000, 0)
            house4.goto(1000, 0)
            house5.goto(1000, 0)
            gmwindow.textinput("", "Oh no! The fish isn't here!\n The thief has now escaped, leaving you ashamed and bewildered...")
            exit()


def backward():
    if player.ycor() >= -230:
        player.shape('sprite_dog5.gif')
        player.sety(player.ycor() - 2.5)
        player.shape('sprite_dog6.gif')
        time.sleep(0.1)
        player.sety(player.ycor() - 2.5)
        player.shape('sprite_dog5.gif')

def hints(x, y):
    global hintnum
    hintnum += 1
    if hintnum == 1:
        gmwindow.textinput("Hint 1:", "Try making a table to help organize your thoughts.\nThis will help speed up the process by a lot.")
    if hintnum == 2:
        gmwindow.textinput("Hint 2:", "Don't randomly guess which house has the fish in it,\ngo through the hints in the code directory very carefully and thoroughly.")
    if hintnum == 3:
        gmwindow.textinput("Hint 3:", "Here's a really big hint: Find the German's house.")
    if hintnum >= 4:
        gmwindow.textinput("No hints left", "I'm sorry, you're on your own now...")
    turtle.listen()
    turtle.onkey(right, 'd')
    turtle.onkey(left, 'a')
    turtle.onkey(forward, 'w')
    turtle.onkey(backward, 's')
    turtle.onkey(right, 'Right')
    turtle.onkey(left, 'Left')
    turtle.onkey(forward, 'Up')
    turtle.onkey(backward, 'Down')
    hint.onclick(hints)
# Here we define different sprites that will move or do something such as houses, the player, and hint button


house1 = turtle.Turtle()
house1.speed(0)
house1.penup()
house1.goto(0, 60)
house1.shape('house.gif')

house2 = turtle.Turtle()
house2.speed(0)
house2.penup()
house2.goto(180, 60)
house2.shape('house.gif')

house3 = turtle.Turtle()
house3.speed(0)
house3.penup()
house3.goto(-180, 60)
house3.shape('house.gif')

house4 = turtle.Turtle()
house4.speed(0)
house4.penup()
house4.goto(360, 60)
house4.shape('house.gif')

house5 = turtle.Turtle()
house5.speed(0)
house5.penup()
house5.goto(-360, 60)
house5.shape('house.gif')

player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape('sprite_dog1.gif')
player.goto(0, -60)

hint = turtle.Turtle()
hint.speed(0)
hint.penup()
hint.goto(200, -200)
hint.shape('Hint.gif')

fish = turtle.Turtle()
fish.hideturtle()
fish.speed(0)
fish.penup()
fish.goto(90, -80)
fish.shape('Fish.gif')

instructions()

# This is how python knows to move the player and houses when the keys are pressed. I am currently using the onkey function as well as the onclick function


turtle.listen()
turtle.onkey(right, 'd')
turtle.onkey(left, 'a')
turtle.onkey(forward, 'w')
turtle.onkey(backward, 's')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')
turtle.onkey(forward, 'Up')
turtle.onkey(backward, 'Down')
hint.onclick(hints)
gmwindow.mainloop()
