# Program to print all prime numbers from 2 to 50

my_list=[]
n=19
for num in range(2, n):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        my_list.append(num)

print(my_list)
