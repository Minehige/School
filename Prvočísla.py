import math
Number = 2
Count = 0
while True:
    Prime = True
    Root = math.floor ( math.sqrt(Number))+2
    for Divider in range(2,Root):
        if Number % Divider==0:
            Prime = False
            break
    if Prime:
        Count += 1
        if Count==500:
        print(Number)
        Count = 0
    Number = Number + 1