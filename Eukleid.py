u = int(input("input Number: "))
w = int(input("input Number: "))
while w!=0:
    r = u % w
    u = w
    w = r
print (u)