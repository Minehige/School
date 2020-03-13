num1 = int(input("Enter The First Number: "))
num2 = int(input("Enter The Second Number: "))

if num1 < num2:
    swap = num1
    num1 = num2
    num2 = swap

print(num1," =",num1//num2,"*",num2,"+",num1%num2)