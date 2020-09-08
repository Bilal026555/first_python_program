def my_encryption(some_string):
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secr_key = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    out_str=""
    for x in some_string:
        char_index=char_set.index(x)
        out_str=out_str+secr_key[char_index]
    return out_str
        
