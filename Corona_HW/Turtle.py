import turtle

shapes = ["Circle","Square","Spiral","Triangle"]
turtle.color(input("Pick a Color: "))
size = int(input("Enter The Size: "))


def Circle(step):
    for x in range (360):
        turtle.right(1)
        turtle.forward(step)

def Square(step):
    for x in range (4):
        turtle.forward(step*100)
        turtle.right(90)

def Spiral(step):
    for x in range (360):
        turtle.left(240/(x+1))
        turtle.forward(step)

def Triangle(step):
    for x in range (3):
        turtle.left(120)
        turtle.forward(step*100)


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

turtle.done()