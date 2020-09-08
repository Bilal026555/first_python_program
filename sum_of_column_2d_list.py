def my_func(list_2d):
    return_list=[]
    for col in range(len(list_2d[0])):
        col_sum=0
        for row in list_2d:
            col_sum=col_sum+row[col]
        return_list.append(col_sum)
    return return_list
            
