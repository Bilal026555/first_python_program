# write a python code that will determine if a number is a prime or not
num=int(input("Please enter a positive number"))
if num > 1:
   for i in range(2,num):
      if (n%i)==0:
         print(num,"is not a prime number")
         break
   else:
      print(num,"is a prime number")
else:
   print(num,"is not a prime number")

