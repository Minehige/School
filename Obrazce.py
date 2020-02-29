num = int(input("Enter The Lenght: "))

def Tree(n):
    for x in range(1,n+1):
        print(" "*(n-x)+"#"*(x*2-1))
    pass

def Box(n):
    print("#"*n)
    for x in range(n-2):
        print("#"+" "*(n-2)+"#")
    print("#"*n)
    pass

Box(num)