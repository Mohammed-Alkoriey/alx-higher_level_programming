#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) >= 0:
        max_ = 0
        for num in my_list:
            if num > max_:
                max_ = num
        return max_
    else:
        return None
