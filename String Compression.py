def str_comp(mystr):
    count = 0
    my_dict = {}
    nstr = ""
    for i in mystr:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    
    for k, v in my_dict.items():
        keys = k
        values = v
        nstr += keys + str(values)
    
    return nstr
print(str_comp("AAAAaaaaBBBBCCCCCDDEEEE"))