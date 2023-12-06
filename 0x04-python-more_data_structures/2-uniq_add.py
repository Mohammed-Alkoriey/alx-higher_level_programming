#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set()
    result = 0
    new_list.append(my_list[0])
    for num in my_list:
        if num not in new_list:
            new_list.add(num)
    for num in new_list:
        result += num
    return result
