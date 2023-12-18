#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    for num in my_list:
        if count < x:
            print(num, end="")
            count += 1
        else:
            break
    print("")
    return count
