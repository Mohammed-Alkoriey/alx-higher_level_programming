#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    while count < x:
        try:
            print(int(my_list[count]), end="")
            count += 1
        except IndexError as e:
            break
    print("")
    return count
