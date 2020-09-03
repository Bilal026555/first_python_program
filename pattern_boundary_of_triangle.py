n=8#int(input("Enter a positive integer n"))
for i in range(n,0,-1):
        if i==n or i==1:
                print("*" * i)
        else:
                print("*" + (" " *(i-2))+"*")

