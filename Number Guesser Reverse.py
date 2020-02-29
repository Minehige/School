import random
print("Think of A number from 1 to 100")
Low = 1
High = 100
Tries = 0
while True:
    Guess = random.randint (Low,High+1)
    print("Is", Guess,"Your Number ?")
    Tries = Tries +1
    Anwser = input("")
    if Anwser in ["Yes","Y"]:
        break
    elif Anwser in ["Low","L"]:
        Low = Guess
        continue
    elif Anwser in ["High","H"]:
        High = Guess
        continue
    else:
        Tries = Tries -1
        print("Non Supported Input")
        continue
print("Well Done Me, Now Prepare For The Machine Uprising")
print("Number Of Tries:",Tries)