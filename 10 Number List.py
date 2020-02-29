Numbers = []
Sqrd = []

for x in range(10):
    print(10-x,"Numbers Left To Enter")
    Numbers.append(int(input("Enter A Number: ")))

for x in range( len(Numbers)):
    Sqrd.append(Numbers[x]**2)

print (Numbers)
print (Sqrd)