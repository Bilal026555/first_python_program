def my_func(list_2d):
    list_row_max=[]
    for row in list_2d:
        row_max_value=0
        for i in range(len(row)):
            #row_max_value=0
            if row[i]>=row_max_value:
                row_max_value=row[i]
        list_row_max.append(row_max_value)
    return list_row_max
