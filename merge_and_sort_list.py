# Write a function that accepts two lists both of
#which contain integers and returns a new list which contains all the elements
#from both lists sorted in descending order.
def my_func(A,B):
    merg_list=[]
    my_list=[]
    for x in A:
        merg_list.append(x)
    for y in B:
        merg_list.append(y)
    while merg_list:
        max_val=merg_list[0]
        for x in merg_list:
            if x>max_val:
                max_val=x
        my_list.append(max_val)
        merg_list.remove(max_val)
    print(my_list)
            
A= [-5, -23, 5, 0]
B=[23, -6, 23, 67]
my_func(A,B)
