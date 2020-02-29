import time
print("Hello Human")
time.sleep(1)
Anws = input("What Is Your Age In Human Years ?")
Age = int(Anws)
time.sleep(0.5)
print("Processing...")
time.sleep(1)
if Age< 18:
    print("No Younglings Allowed Beyond This Point")
    break
else:
    print("Wonderful, You Make Continue Human")