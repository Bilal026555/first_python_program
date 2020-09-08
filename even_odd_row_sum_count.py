def my_func(list_2d):
    count_even_row=0
    count_odd_row=0
    for row in list_2d:
        row_sum=0
        for i in range(len(row)):
            row_sum=row_sum+row[i]
        if row_sum%2==0:
            count_even_row=count_even_row+1
        else:
            count_odd_row=count_odd_row+1
    return [count_even_row,count_odd_row]
