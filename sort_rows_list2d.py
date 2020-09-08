def my_func(list_2d):
    list_sorted=[]
    for row in list_2d:
        temp_rows=[]
        #temp_list_sorted
        for i in range(len(row)):
            temp_rows.append(row[i])
        temp_rows_sorted=sorted(temp_rows,reverse=True)
        list_sorted.append(temp_rows_sorted)
    return list_sorted
            
