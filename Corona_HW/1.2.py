divider = int(input("Enter Your Number: "))
num = 101
Count = 0

while Count != 5:
    if num%divider == 0:
        print(num,end=" ")
        Count = Count + 1
    num = num + 1
