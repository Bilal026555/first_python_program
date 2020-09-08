def my_func(list_2d):
    list_1d=[]
    for row in list_2d:
        for i in range(len(row)):
            list_1d.append(row[i])
    list_sorted=sorted(list_1d)
    return list_sorted
            
