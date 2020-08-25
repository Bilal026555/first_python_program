# write a python function that sort the element of a list in ascending order
def my_func(data_list):
    my_list=[]
    while data_list:
        min_val=data_list[0]
        for x in data_list:
            if x< min_val:
                min_val=x
        my_list.append(min_val)
        data_list.remove(min_val)
    print(my_list)

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
my_func(data_list)
