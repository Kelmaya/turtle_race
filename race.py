import random
import time
import turtle

def makeTurtle(racer,color,x,y):
    racer.turtlesize(2)
    racer.pensize(5)
    racer.shape("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(x,y)
    racer.pendown()
    
def spash_title():
    title_content = ["Python Project 4", "Turtle Race", "Kelvin Amaya"]
    for x in title_content:
        turtle.write(x, False, align="center",font=("Arial", 50, "normal"))
        turtle.forward(80)

def splash():
    turtle.Screen().bgcolor("black")
    turtle.pencolor("white")
    turtle.penup()
    turtle.hideturtle()
    turtle.right(90)
    spash_title()
    time.sleep(2)

def raceSetup():
    turtle.clearscreen()
    turtle.setup(width=700,height=700)
    turtle.Screen().bgpic("C:\\Users\\12016\\Desktop\\[Year Up]\\CIS 401\\Week 11\\Project\\track.gif")
    turtle.clear()
    
    firstTurtle = turtle.Turtle()
    secondTurtle = turtle.Turtle()
    thirdTurtle = turtle.Turtle()
    fourthTurtle = turtle.Turtle()
    fifthTurtle = turtle.Turtle()
    sixthTurtle = turtle.Turtle()
    seventhTurtle = turtle.Turtle()
    eighthTurtle = turtle.Turtle()

    makeTurtle(firstTurtle,"cyan",-300,150)
    makeTurtle(secondTurtle,"yellow",-300,105)
    makeTurtle(thirdTurtle,"violet",-300,65)
    makeTurtle(fourthTurtle,"green",-300,20)
    makeTurtle(fifthTurtle,"blue",-300,-25)
    makeTurtle(sixthTurtle,"red",-300,-70)
    makeTurtle(seventhTurtle,"black",-300,-115)
    makeTurtle(eighthTurtle,"orange",-300,-160)
    raceStart(firstTurtle, secondTurtle, thirdTurtle, fourthTurtle,fifthTurtle,sixthTurtle,seventhTurtle,eighthTurtle)
    

def raceStart(firstTurtle, secondTurtle, thirdTurtle, fourthTurtle,fifthTurtle,sixthTurtle,seventhTurtle,eighthTurtle):
    turtlecollection = [firstTurtle, secondTurtle, thirdTurtle, fourthTurtle,fifthTurtle, sixthTurtle, seventhTurtle,eighthTurtle]
    ending = False
    while True:
        num = 1
        for i in turtlecollection:          
            ran = random.randint(1, 20)
            if(i.xcor()>=175):
                i.write("Winner",False, align="left",font=("Arial", 20, "bold"))
                time.sleep(3)
                winner(i,"Turtle "+ str(num))
                ending=True
                break
            i.forward(ran)
            num += 1
        if(ending):
            break
def winner(winner,name):
    turtle.clearscreen()
    turtle.Screen().bgpic("C:\\Users\\12016\\Desktop\\[Year Up]\\CIS 401\\Week 11\\Project\\winner.gif")
    turtle.clear()
    winner.color("black")
    winner.penup()
    winner.goto(0,-300)
    winner.pendown()
    winner.write(name,False, align="center",font=("Arial", 50, "bold"))

splash()
raceSetup()
turtle.done()