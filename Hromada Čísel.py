count = int(input("How Many Number Do You Wish To Enter? "))
total = 0
for x in range(count):
    number = int(input("Enter A Number: "))
    total = total + number
    if x == 0:
        low = number
    else:
        if number < low:
            low = number
print("The Sum Of Your Numbers Is: "+str(total))
print("The Average Value Of Your Numbers Is: "+str(total/count))
print("The Lowest Value Number You Entered Is: "+str(low))