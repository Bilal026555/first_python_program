def my_func(list_2d):
    #No_even_numbers=False
    #list_even_numbers=[]
    max_even=0
    if list_2d==[[]]:
        return None
    else:
        for rows in list_2d:
            for i in range(len(rows)):
                if rows[i]%2==0:
                    #No_even_numbers=True
                    temp=rows[i]
                    if temp>=max_even:
                        max_even=temp
        if max_even>0:
            return max_even
        else:
            return None
                
                    
