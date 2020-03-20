import turtle
import math


size = int(input("Size: "))

#circuit = size*360
#radius = circuit/(2*math.pi)
#print (radius)
#turtle.sety(radius)

turtle.sety((size*360/(2*math.pi)))

print(turtle.ycor())

for x in range (360):
    turtle.forward(size)
    turtle.right(1)