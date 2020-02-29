num1 = int(input("Enter The First Number "))
num2 = int(input("Enter The Second Number "))

if num1 > num2:
    swap = num2
    num2 = num1
    num1 = swap

for x in range(num1, num2+1):
    print(x)