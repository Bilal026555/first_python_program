n=int(input("Enter a positive integer greater than orequal to 3"))
#n=7
b=0
for i in range(n,0,-1):
   b=b+1
   for j in range (1,i+1):
      print(b,end=" ")
   print("")
