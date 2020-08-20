def my_func(n):
    new_list=[]
    sum_new_list=0
    for i in range(1,n):
        if n%i==0:
            new_list.append(i)
    for j in range(len(new_list)):
        sum_new_list=sum_new_list+new_list[j]
    if sum_new_list==n:
        return True
    else:
        return False
