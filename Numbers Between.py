Num1 = int(input("Enter The First Number Human "))
Num2 = int(input("Enter The Second Number Human "))
if Num1>Num2:
    Swap = Num1
    Num1 = Num2
    Num2 = Swap
print("Your Numbers")
print(Num1)
print(Num2)
for x in range(Num1,Num2+1):
    print (x)