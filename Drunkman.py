import random
import time

Lenght = int(input("Enter The Distance: "))
Steps = int(input("Enter The Drunk Mans Energy: "))


def Drunk(Distance,Energy):
    Position = Distance//2
    while Position != 1 and Position != Distance:
        if Energy != 0: 
            Move = random.randint (0,1)
            if Move == 0:
                Position = Position - 1
            else:
                Position = Position + 1
            print("Home"+"_"*(Position-1)+"O"+"_"*(Distance-Position)+"Pub")
            time.sleep(0.1)
            Energy = Energy - 1
            if Energy == 0:
                print("You Fell Asleep On The Way")
                break
    if Position == 1:
        print("Good, You Reached Home")
    if Position == Distance:
        print("Ended In The Pub Again")

Drunk(Lenght,Steps)
