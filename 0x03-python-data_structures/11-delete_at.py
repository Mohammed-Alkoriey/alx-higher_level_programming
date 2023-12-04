#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = []
        x = 0
        for num in my_list:
            if x == idx:
                x += 1
                continue
            else:
                new_list.append(num)
                x += 1
        return new_list
