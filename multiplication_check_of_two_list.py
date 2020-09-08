def my_func(a,b):
    len_a_col=len(a[0])
    len_b_row=len(b)
    if len_a_col==len_b_row:
        return True 
    else:
        return False
