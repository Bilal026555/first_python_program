def my_func(list_2d):
    list_col_max=[]
    for c in range(len(list_2d[0])):
        col_max=0
        for row in list_2d:
            #col_max=0
            if row[c]>=col_max:
                col_max=row[c]
        list_col_max.append(col_max)
    return list_col_max
