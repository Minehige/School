import random
Tries = 1
Number = random.randint (1,101)
while True:
    Guess = int(input("Enter Your Guess: "))
    if Guess == Number:
        break
    else:
        Tries = Tries+1
        if Guess > Number:
            print("Too High")
        else:
            print("Too Low")
print("Good, You Guessed The Number Human, it was:", Number)
print("Number od Tries:",Tries)