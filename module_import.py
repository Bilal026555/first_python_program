# define some functions that show how to import python modules
def my_sqrt(x):
   import math as mt
   return mt.sqrt(x)
def my_factorial(x):
   from math import factorial
   return factorial(x)
def my_prime_num(n):
   import sympy
   if sympy.isprime(n):
      print(n,"is a prime number")
   else:
      print(n,"is not a prime number")
n=5
print("The square root of",n,"is",my_sqrt(n))
print("The factorial value of",n,"is",my_factorial(n))
print("Prime number test")
my_prime_num(n)
