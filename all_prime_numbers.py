# Program to print all prime numbers from 2 to 50

# To take input from the user
#num = int(input("Enter a number: "))
start_num=2
end_num=10
for num in range(start_num,end_num+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
