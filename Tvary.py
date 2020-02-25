Count = int(input("Number:"))

def Tree(num): 
    for x in range(1,num+1):
        print(" "*(num-x)+"#"*(2*x-1))

def Box(num):
    print("#"*num)
    for x in range(num-2):
        print("#"+" "*(num-2)+"#")
    print("#"*num)

Tree(Count)
print()
Box(Count)