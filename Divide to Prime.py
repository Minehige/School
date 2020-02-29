num = int(input("Enter Your Number "))
prime = []

while num>1:
    for div in range (2,num+1):
        if num % div == 0:
            num = num // div
            prime.append(div)
            break

print(prime)