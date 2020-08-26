def my_func(list_a):
    my_list=[]
    l=len(list_a)
    for i in range(0,l):
        my_list.append(list_a[l-1-i])
    return my_list
        
