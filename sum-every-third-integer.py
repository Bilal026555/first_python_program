#Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)
import math
#math.ceil(x)
sumin=0
i=1
N=1001
qt=N/3
n=math.ceil(qt)
#tolterm=res/2
while (i<=n):
    sumin=sumin+(3*i-2)
    i=i+1
print(sumin)
