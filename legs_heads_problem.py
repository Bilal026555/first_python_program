def my_func(heads,legs):
   # lets no. of chicken x
   #no. of dogs y
   # x+y=a and 2x+4y=b
   # x=a-y
   for y in range(0,heads+1):
      x=heads-y
      if 2*x+4*y==legs:
         return [x,y]
   return [None,None]
print(my_func(5,12))
