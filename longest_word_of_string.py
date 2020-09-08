def find_longest_word(some_string):
    str_new=some_string.split()
    count=0
    #lon
    for x in str_new:
        if len(x)>=count:
            count=len(x)
            temp_word=x
    return temp_word
