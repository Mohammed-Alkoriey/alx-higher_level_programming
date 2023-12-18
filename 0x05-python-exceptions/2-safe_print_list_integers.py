#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0

    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
            printed += 1
        except (ValueError, TypeError):
            count += 1
            pass
        except IndexError as er:
            raise er
    print("")
    return printed
