import turtle

total = 0
size = int(input("Size: "))

print(turtle.pos())


for x in range (90,0,-1):
    total = total + (size*(x/90))
    print(x," : ",size*(x/90))

print (total)

turtle.sety(total)

print (turtle.ycor())

for x in range (360):
    turtle.forward(size)
    turtle.right(1)

turtle.done()