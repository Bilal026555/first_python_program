n=int(input("Enter a positive integer greater than orequal to 3"))
for i in range(1, n+1):
   # num = 1
   a="*"
   b=" "
   for j in range(n, 0, -1):
      if i >= j:
         print(a, end=' ')
      else:
         print(b, end=' ')
   print("")
         
    
