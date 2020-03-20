import turtle
import math


def Circle(step):
    turtle.penup()
    turtle.sety((step*360/(2*math.pi)))
    turtle.pendown()
    for x in range (360):
        turtle.forward(step)
        turtle.right(1)

def Square(step):
    turtle.penup()
    turtle.sety(step*-50)
    turtle.setx(step*-50)
    turtle.pendown()
    for x in range (4):
        turtle.forward(step*100)
        turtle.left(90)

def Spiral(step):
    for x in range (360):
        turtle.forward(step)
        turtle.left(240/(x+1))

def Triangle(step):
    turtle.penup()
    turtle.setx(step*-50)
    turtle.sety((math.sqrt(((step*100)**2)-((step*50)**2)))*-(1/3))
    turtle.pendown()
    for x in range (3):
        turtle.forward(step*100)
        turtle.left(120)

def Hexagon(step):
    turtle.penup()
    turtle.setx(step*-25)
    turtle.sety((math.sqrt(((step*50)**2)-((step*25)**2)))*-1)
    turtle.pendown()
    for x in range (6):
        turtle.forward(step*50)
        turtle.left(60)


shapes = ["Circle","Square","Spiral","Triangle","Hexagon"]
turtle.color(input("Pick a Color: "))
size = int(input("Enter The Size: "))
print("Avalible Shapes:",shapes)
shape = input("Pick a Shape: ")

if shape == "Circle":
    Circle(size)
elif shape == "Square":
    Square(size)
elif shape == "Spiral":
    Spiral(size)
elif shape == "Triangle":
    Triangle(size)
elif shape == "Hexagon":
    Hexagon(size)

turtle.done()