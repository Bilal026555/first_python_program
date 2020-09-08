def test_for_anagrams(my_string1, my_string2):
    s1=list(my_string1.lower())
    s2=list(my_string2.lower())
    s1_sorted=sorted(s1)
    s2_sorted=sorted(s2)
    if s1_sorted==s2_sorted:
        return True 
    else:
        return False
