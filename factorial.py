# Type your code here
user_input=input("Enter an positive integer")
n=int(user_input)
fact=1;
if n<0:
    print("Sorry, factorial does not exit for negative values")
elif n==0:
    print("factorial of 0 is 0")
else:
    i=1
    while (i<=n):
        fact=i*fact
        i=i+1
print(fact)
